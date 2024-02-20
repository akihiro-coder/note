## Basic of HTML
- 段落
    - p
- 見出し
    - h1 ~ h6 
- リンク
    - a
    - href属性にリンクを書く
- 画像
    - img
    - src属性に画像パスを書く
- リスト
    - li
```html
<!-- htmlコメント -->

<!-- ul要素で囲むと黒点が先頭につく -->
<ul>
    <li>HTML</li>
    <li>Python</li>
</ul>

<!-- ol要素で囲むと数字が連番でつく -->
<ol>
    <li>HTML</li>
    <li>Python</li>
</ol>
```
- HTMLの全体構造
    - <html>要素の中に<head>要素と<body>要素が必要です。<head>要素にはページに関する情報、<body>要素には実際に表示したい内容を書きます。
- HTMLバージョンを指定する
    - <!doctype html>の部分はDOCTYPE宣言と呼ばれるもので、HTMLのバージョンを宣言するためのもの
    - 最新バージョンのHTMLを使うため、<!doctype html>を使用する。
- <head>要素
    - <head>要素にはWebページの設定に関する情報を書いていきます。
    - <head>要素内に記述した内容はWebページには表示されません。
```html
<head>
    <!-- 文字コード -->
    <meta charset="utf-8">
    <!-- ページタイトル -->
    <title>Progate</title>
    <!-- cssの読み込み -->
    <!-- rel="stylesheet": cssファイルを読み込む宣言 -->
    <!-- href="stylesheet.css": 読み込むcssのファイル名 -->
    <link rel="stylesheet" href="stylesheet.css">
</head>
```



## Basic of CSS
###  cssの基本形
```css
/* cssコメント */
h1 {
    color: #ff0000;   
    font-size: 10px;
    font-family: serif;
    background-color: #ddd;
    width: 500px;
    height: 80px;
}
```
### 様々なプロパティ
    - color: 文字の色
    - font-size: 文字の大きさ
    - font-family: フォントの種類
    - background-color: 背景色
    - width, height: 横幅、高さ

### 特定のリスト要素に色をつける
```html
<!-- class属性で名前をつける -->
<ul>
    <li class="selected">HTML</li>
    <li>PHP</li>
    <li>Python</li>
</ul>
```
```css
/* class属性名に.をつけてcssをあてる */
.selected {
    color: red;
}
```

### ヘッダー
```html
<div class="header">
    <ul>
        <li>HTML</li>
        <li>Python</li>
    </ul>
</div>
```
```css
li {
    // リストのマークをなくす
    list-style: none;
    // 指定した要素を横並びにする
    float: left;
}
```

### paddingの指定(marginも同じ)
```css
li {
    // 時計回りで指定する方法
    padding: top right bottom left;

    // 上下　左右　の順番で指定する方法
    padding: top-bottom right-left;

    // 上右下左の順番で指定する方法
    padding-top: ~~px;
    padding-right: ~~px;
    padding-bottom: ~~px;
    padding-left: ~~px;
}
```

### フッター
```html
<div>
    <div class="footer">
        <div class="footer-logo">LOGO</div>
        <div class="footer-list">
            <ul>
                <li>会社概要</li>
                <li></li>
                <li></li>
            </ul>
        </div>
    </div>
</div>
```

```css
// footer-listの<li>要素にのみcssを適用する
.footer-list li {
    color: red;
}
```

### ロゴとリストの配置
    - cssでfloat:left;を指定すると、要素が左に配置される
    - cssでfloat:right;を指定すると、要素が右に配置される


## mainの構造
- (前提)一般的な会社用のページは、header, main, footerの３つのクラスで構成されている。いずれもdivタグ内のclassに指定する。
- main要素は、copy-container, contents, contact-formの３つのクラスで構成されている

## 文中の一部にcssを適用させる
- 文中の一部にcssを適用させたい場合は、<span>要素で囲む
```html
<h1>
    ようこそ、<span>Japan</span>へ
</h1>
```
```css
span {
    color: #ff0000;
}
```

## 改行される要素、改行されない要素
- 前後で改行が入り、親要素の幅いっぱいに広がる要素を「ブロック要素」という。
    - div, h1, pタグは全てブロック要素
- 改行されない要素を「インライン要素」という。
    - span, aタグなどは全てインライン要素

## ボーダー(枠線)
```html
<div class="logo1">
    Progate
</div>

<div class="logo2">
    Progate
</div>
```
```css
.logo1 {
    /* 枠線: 太さ 種類 色; */
    border: 5px solid red;

    /* ボーダーの内側全体に10pxの余白を追加 */
    padding: 10px;

    /* ボーダーの外側全体に10pxの余白を追加 */
    margin: 10px;

}
.logo2 {
    /* 下線: 太さ 種類 色; */
    border-bottom: 5px solid red;
}
```

## 入力欄
- input要素は１行のテキスト入力を受け取るための要素です。
    - 送信ボタンもinputタグを使用する。
    - valueプロパティ属性にボタンに表示する名前を記述する
```html
<input type="button" value="保存">
<textarea></textarea>
```
```css
/* , で別のセレクタに同じcssを適用できる */
input, textarea {
    border: 5px solid red;
}
```
- textarea要素は複数行のテキスト入力を受け取るための要素です。



































