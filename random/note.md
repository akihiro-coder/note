# 名前解決の方法　Ubuntu
```sh
sudo vim /etc/hosts
ip, サブドメイン 追加
```
- サブドメインとは　→　[URLを構成する５つの要素](https://blog.hubspot.jp/marketing/parts-url#:~:text=URL%E3%81%AE%E6%A7%8B%E6%88%90%E8%A6%81%E7%B4%A0,%E8%A6%81%E7%B4%A0%E3%81%A7%E6%A7%8B%E6%88%90%E3%81%95%E3%82%8C%E3%81%BE%E3%81%99%E3%80%82)
- 名前解決によって、サブドメイン名で紐付いたipアドレスにアクセスできる


# python bytes型について
- 参考サイト　→　[pythonのbytes型について初心者向けに書いてみた](https://dev.classmethod.jp/articles/python-bytes-newshiro)
    - encodeメソッドの動作を手動でやって動作確認しているサイト　
## bytes型とは
- バイナリデータを扱うデータ型
- 文字列の文字コードを表している
- pythonドキュメントによると、「バイナリデータを操作するためのコア組み込み型はbytesおよびbytearrayです。」とのこと。
## str.encode()で出来ること
- str型をbytes型に変換することができる
- 引数を指定しない場合は、UTF-8を文字コードとして選択するようになっている
- 文字列　⇨　Unicode　⇨　UTF-8　の変換をしてくれる




# opencvの商用利用
- opencvは商用利用可能
- opencv contribは商用利用一部不可
- 参考リンク　⇨　[OpenCVの商用利用](https://ari23ant.com/entry/opencv-license#OpenCV)
