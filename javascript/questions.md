1. 中級編 webページを作ろう　レッスン一覧を作ろう
- HTML等の表示にマウスを当てたら説明文が表示されるようにする
- うまく動かない理由が分からない

```html
<p class="text-contents">説明文</p>
```
- 自分のコード
```css
.text-contents {
    display: none;
}
```
```javascript
$('.lesson').hover(
    function(){
        $(this).find('.text-contents').css('display', 'block');
    },
    function(){
        $(this).find('.text-contents').css('display', 'none');
    }
)
```
- progateの回答
```css
.text-contents {
    display: none;
}

.text-active {
    display: block;
}
```
```javascript
$('.lesson').hover(
    function(){
        $(this).find('.text-contents').addClass('text-active');
    },
    function(){
        $(this).find('.text-contents').removeClass('text-active');
    }
)
```
