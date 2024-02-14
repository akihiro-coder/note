# githubと連携 & sshでpushまで
1. ssh pubkeyがgithubと共有されていることを確認する。共有されていない場合（新しいパソコンは共有されていない）は、[GitHubでssh接続する手順~公開鍵・秘密鍵の生成から~](https://qiita.com/shizuma/items/2b2f873a0034839e47ce)を参考に、共有鍵をgithubで共有する設定を行う。
2. リポジトリはsshでクローンし直す
3. 編集内容をpushする

# command
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
