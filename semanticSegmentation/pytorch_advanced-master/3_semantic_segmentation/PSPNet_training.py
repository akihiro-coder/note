import random
import math
import pandas as pd
import numpy as np

import torch
import torch.utils.data as data
import torch.nn as nn
import torch.nn.init as init
import torch.nn.functional as F
import torch.optim as optim

from utils.dataloader import make_datapath_list, DataTransform, VOCDataset
from utils.pspnet import PSPNet

# Setup seeds
torch.manual_seed(1234)
np.random.seed(1234)
random.seed(1234)

# make file path list
rootpath = './data/VOCdevkit/VOC2012/'
train_img_list, train_anno_list, val_img_list, val_anno_list = make_datapath_list(rootpath=rootpath)


# make dataset

# (RGB)の色の平均値と標準偏差
color_mean = (0.485, 0.456, 0.406)
color_std = (0.229, 0.224, 0.225)
train_dataset = VOCDataset(train_img_list, train_anno_list, phase='train', transform=DataTransform(input_size=475, color_mean=color_mean, color_std=color_std))
val_dataset = VOCDataset(val_img_list, val_anno_list, phase='val', transform=DataTransform(input_size=475, color_mean=color_mean, color_std=color_std))


# make dataloader
batch_size = 8

train_dataloader = data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

val_dataloader = data.DataLoader(train_dataset, batch_size=batch_size, shuffle=False)

dataloaders_dict = {'train': train_dataloader, 'val': val_dataloader}


# make network model
# use pre-trained model by ADE20K dataset
net = PSPNet(n_classes=150)

state_dict = torch.load('./weights/pspnet50_ADE20K.pth')
net.load_state_dict(state_dict)

# 分類用の畳み込み層を、出力数21のものに付け替える
n_classes = 21
net.decode_feature.classification = nn.Conv2d(in_channels = 512, out_channels=n_classes, kernel_size=1, stride=1, padding=0)
net.aux.classification = nn.Conv2d(in_channels=256, out_channels=n_classes, kernel_size=1, stride=1, padding=0)


# 付け替えた畳み込み層を初期化する。活性化関数がシグモイド関数なのでXavierを使用する。
def weights_init(m):
    if isinstance(m, nn.Conv2d):
        nn.init.xavier_normal_(m.weight.data)
        if m.bias is not None: # バイアス項がある場合
            nn.init.constant_(m.bias, 0.0)

net.decode_feature.classification.apply(weights_init)
net.aux.classification.apply(weights_init)

print('ネットワーク設定完了：学習済みの重みをロードしました')



# 損失関数を定義
class PSPLoss(nn.Module):
    def __init__(self, aux_weight=0.4): # メインの損失とAuxLossの損失の和をトータルの損失とするが、係数0.4をかけて、その重みをメインの損失よりも小さくしておく
        super(PSPLoss, self).__init__()
        self.aux_loss = aux_weight # aux_lossの重み

    def forward(self, outputs, targets):
        loss = F.cross_entropy(outputs[0], targets, redecution='mean')
        loss_aux = F.cross_entropy(outputs[1], targets, reduction='mean')

        return loss+self.aux_weights*loss_aux


criterion = PSPLoss(aux_weight=0.4)



# 最適化手法を設定
# ファインチューニングなので、入力に近いモジュールの学習率は小さく、付け替えた畳み込み層を持つdecoder, auxlossモジュールは大きく設定している
optimizer = optim.SGD([
    {'params': net.feature_conv.parameters(), 'lr': 1e-3},
    {'params': net.feature_res_1.parameters(), 'lr': 1e-3},
    {'params': net.feature_res_2.parameters(), 'lr': 1e-3},
    {'params': net.feature_dilated_res_1.parameters(), 'lr': 1e-3},
    {'params': net.feature_dilated_res_2.parameters(), 'lr': 1e-3},
    {'params': net.pyramid_pooling.parameters(), 'lr': 1e-3},
    {'params': net.decode_feature.parameters(), 'lr': 1e-2},
    {'params': net.aux.parameters(), 'lr': 1e-2},
], momentum=0.9, weight_decay=0.0001)

# スケジューラーの設定
# 最大エポック数を30とし、エポックを経る毎に徐々に学習率が小さくなるように設定
def lambda_epoch(epoch):
        max_epoch = 30
        return math.pow((1-epoch/max_epoch), 0.9)


# epochに応じて学習率を変化させる機能 スケジューラ
# lambda_epochの内容に従い、インスタンスoptimizerの学習率を変化させる
scheduler = optim.lr_scheduler.LambdaLR(optimizer, lr_lambda=lambda_epoch)




# モデルを学習させる関数を作成

def train_model(net, dataloaders_dict, criterion, scheduler, optimizer, num_epochs):
    # GPUが使えるか確認
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print('使用デバイス：', device)

    # ネットワークをGPUへ
    net.to(device)

    # ネットワークがある程度固定であれば、高速化させる

