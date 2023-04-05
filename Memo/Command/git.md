# Git command
## ブランチを一時的に過去のコミットに戻す
- git checkout <commit name>
- 最新の状態に戻す
  - git checkout <branch name>
- commit nameの検索
  - git log
- 参考文献
  - [qiita 一時的に過去のcommitに戻りたい](https://qiita.com/yu_andante/items/866e45d771b28cf05bf2)

## modifiedなファイル全てをgit addする方法
- git add -u
- 使いどころ
  - ファイル名を変更、ディレクトリ名を変更、ディレクトリ移動等の時など
