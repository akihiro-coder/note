# githubと連携 & sshでpushまで
1. ssh pubkeyがgithubと共有されていることを確認する。共有されていない場合（新しいパソコンは共有されていない）は、[GitHubでssh接続する手順~公開鍵・秘密鍵の生成から~](https://qiita.com/shizuma/items/2b2f873a0034839e47ce)を参考に、共有鍵をgithubで共有する設定を行う。
2. リポジトリはsshでクローンし直す
3. 編集内容をpushする


# wget ~~~.zipの罠
- git cloneではなく、wget ~~~.zip && unzip ~~~.zipでリポジトリをローカルに落としてくる
- 当たり前だが、この方法でリポジトリを持ってくると、gitコマンドが使えないから、注意が必要になる
- [車色検出デモ](https://github.com/openvinotoolkit/openvino/blob/master/docs/dev/build_linux.md)
```sh
git clone https://github.com/openvinotoolkit/openvino.git
cd openvino
git submodule update --init --recursive
```
- zipファイルで持ってくると、最後のsubmoduleコマンドが効かない
- これで30分ほど失った

# git Commands
- チームメンバーが開発中のリモートブランチ(origin/hoge)をローカルに持ってくる方法
```zsh
" リモート追跡ブランチを最新にする
git fetch 

" リモート追跡ブランチが更新されたか確認
git branch -a

" origin/hogeブランチのコピーをhogeブランチとしてブランチを作成して、チェックアウトする
git checkout -b hoge origin/hoge 

```

- 別ブランチにあるファイルを、今いるブランチに持ってくる方法
    - 参照：[Gitで別ブランチから特定のファイルやディレクトリを取得するコマンド](https://t-cr.jp/memo/1a817a9f72658927a)
```sh
" branchAにfileがあるか確認
git show <branchA>:<file path> 

" branchB(ファイルを持ってきて保存したいブランチ)に移動
git checkout <branchB>

" branchAのfileをbranchBに持ってくる
git checkout <branchA> path/to/file
```

- 特定のファイルだけ過去のコミットに戻す
```sh
" fileのコミット履歴を探索
git log -p <file path>

" fileだけ過去のコミットに戻す
git checkout <commit ID> <file path>
```

- 編集したファイルと削除したファイルを同時にステージングする
```sh
git add -u
```

- git stash
    - コミットのタイミングではないけど、突然、他のブランチで作業を行わないといけなくなった時
    - 作業するブランチを間違えた時
```sh
" message付きでステージング前のファイルを退避
git stash save "message"  

" 退避した作業一覧を見る　
git stash list

" 退避した作業を戻す
git stash apply stash@{number}
" 退避した作業を戻すと同時に、stashのリストから削除する。
git stash pop stash@{number}
```

- ステージング前にファイルの変更分を取り消す
```sh
git checkout <file path>
```
- 特定のファイルの変更を取り消す(ステージング前のファイル)
```sh
git checkout @ filename
```
- 複数のファイルの変更を取り消す(ステージング前のファイル)
```sh
git checkout @ filename1 filename2
```
- 全てのファイルの変更を取り消す(ステージング前のファイル)
```sh
git reset -hard @
```
- [ステージング前の変更を取り消す（@の意味なども書いてある）](https://prograshi.com/general/git/cancel-changes-before-stage/)

- clone後にmainブランチ以外のブランチにチェックアウトする
```sh
git fetch
git checkout -b <develop> origin/develop
```

- ２つのリモートブランチの差分を確認
```sh
git fetch
git diff origin/a origin/b
```


- すでにgit管理下にあるファイルやディレクトリをgit管理対象から外す
    - [git管理下にあるファイルやディレクトリを管理対象から外す](https://kleinblog.net/git-ignore.html)
```sh
git rm --cached filename (ファイルを外す)

git rm --cached directoryname (ディレクトリを外す)
```


- コミットの取り消し
    - [git resetでどのオプションを指定するべきか、シチュエーション別に分けてみる](https://qiita.com/kmagai/items/6b4bfe3fddb00769aec4)
    - [コミットの取り消し、打ち消し、上書き](https://qiita.com/shuntaro_tamura/items/06281261d893acf049ed)
```sh
HEAD^    直前のコミットを意味する
HEAD~{n} n個前のコミットを意味する

git reset --soft HEAD^  直前のコミットを取り消し、ステージングを残る
git reset --mixed HEAD^ 直前のコミットを取り消し、ステージングを取り消し、ワークディレクトリは残る
git reset --hard HEAD^  直前のコミットを取り消し、ステージングを取り消し、ワークディレクトリを取り消す
```


- ブランチ間の差分のとり方
```sh
git diff branchA branchB
```

- 直前にステージングしたファイルのステージングの取り消し
```sh
git reset --mixed HEAD filename
```

- ローカルのブランチを削除する
    - ちなみに、削除対象のブランチにいながら削除することは出来ないため、削除対象ブランチ以外のブランチにチェックアウトしてから、削除対象のブランチを削除すること。
```sh
git branch -d branchname
```
