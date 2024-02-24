# console.log
- console.log(''), console.log("") のどちらでもいい
- ;で終わること

# コメントアウト　
- 先頭に//を書くとその行はコメントとみなされる　


# let, constの違い　
- let　変数定義をするもの。値を更新できる。
- const　定数定義をするもの。値を更新できない。


# テンプレートリテラル(ES6)のポイント
- 文字列全体をバッククオートで囲む
- 変数は${変数(or 定数)}とする。
```javascript
const name = 'あきひろ';
console.log('こんにちは、' + name + 'さん');
// テンプレートリテラル　
console.log(`こんにちは、${name}さん`);
```


# 条件分岐
## if
- かつ　→　&&
- または　→　||
```javascript
const num = 12;
if (num > 10){
    console.log('numは10より大きい');
}else if(num > 5 && num <= 10){
    console.log('numは5より大きく10以下');
}else {
    console.log('numは5以下')
} // ←　ここにセミコロンは不要
```

## switch
- breakが無いと次のcase文も処理される。
- caseのどれにも一致しなかったときはdefault文が実行される
```javascript
const color = 'red';
switch(color){
    case 'red':
        console.log('stop!');
        break;
    case 'blue':
        console.log('go!');
        break;
    default:
        console.log('Be carefull!')
        break;
} // ←　ここにセミコロンは不要
```


# 繰り返し処理
## while
```javascript 
let number = 1;
while (number < 100){
    console.log(number);
    number += 1;
} // ←　ここにセミコロンは不要
```

## for
```javascript
for (let number = 1; number < 100; number += 1){
    console.log(number);
} // ←　ここにセミコロンは不要
// number += 1 →　number++と書くことも可能
```


# 配列
- 要素の更新はできる
- 定数に再代入はできない
```javascript
const fruits = ['apple', 'banana', 'orange'];
fruits[0] = 'grape'; // 要素の更新はできる
// fruits = ['grape'];  // 定数に再代入はできない

// 要素を１つずつ取り出してみる
// やり方①   要素番号を指定
console.log(fruits[0]);
console.log(fruits[1]);
console.log(fruits[2]);

// やり方②  for文
for (let i = 0; i < 3; i++){
    console.log(fruits[i]);
}

// やり方③  for文+条件式にlength使用
for (let i = 0; i < fruits.length; i++){
    console.log(fruits[i]);
}
```


# オブジェクト
- それぞれの値にプロパティと呼ばれる名前をつけて管理する
- 一方、配列は複数の値を並べて管理する
- オブジェクトの値を取り出すには、対応するプロパティ名を用いて、オブジェクト.プロパティ名とする。
```javascript
const item = {name: 'kunai', price: 100};
console.log(item.name); // このようにアクセスする
item.price = 200; // 更新ができる

// オブジェクトを要素に持つ配列も定義できる
const items = [
    {name: 'kunai', price: 100},
    {name: 'shuriken', price:50}
    ];
console.log(items[0].name); // 'kunai'が出力される
```

# undefined
```javascript
const items = [
    {name: 'kunai', price: 100},
    {name: 'shuriken', price:50},
    {name: 'kibakufuda'}
    ];
for (let i = 0; i < items.length; i++){
    const item = items;
    if (item.price == undefined){
        console.log('undefined');
    }else{
        console.log(item.price);
    }
}
```


# ちょっとだけ複雑なオブジェクトデータ管理　
```javascript
const items = {
    name: 'kunai',
    num: 5,
    foods: ['Udon', 'Ramen', 'Banana'], //配列をオブジェクトの値に定義することが可能
    favorite: {
        morning: 'Banana',
        noon: 'Ramen',
        evening: 'Udon'
    } // オブジェクトをオブジェクトの値に定義することも可能
};

console.log(items.foods[1]); // 'Ramen'が出力される
console.log(items.favorite.noon); // 'Ramen'が出力される
```



# 関数
- 関数を定数に代入することで関数を定義する
- ES5とES6では書き方が異なる
```javascript
// ES5以前の書き方　
const hello = function(name, age){
    console.log(`${name}さん、こんにちは`);
    console.log(`${name}さん、${age}歳なんですね`);
}

// ES6での書き方
const hello = (name, age) => {
    console.log(`${name}さん、こんにちは`);
    console.log(`${name}さん、${age}歳なんですね`);
}

const add = (num1, num2) => {
    return num1 + num2;
}

const sum = add(10, 20);
```


# ==, ===の違い
- 参考→　[JavaScript 忘れがちな　=== と == の違い](https://qiita.com/PianoScoreJP/items/e43d70ec188c6fed73ed)
> == 等価演算子
> 数値と文字列を比較するとき、文字列は数値に変換されます。JavaScript は文字列の数値リテラルを Number 型の数値に変換しようと試みます。最初に、その文字列の数値リテラルから数学的な値を引き出します。次に、最も近い Number 型の値にこの値を丸めます。

> === 厳密等価演算子
> オペランド同士が、型を変換することなく(上に示した通り)厳密に等しいならば真を返します。

```javascript
var a = '1';
var b = 1;

console.log(a == b); // true 文字列と数値の比較の場合、文字列を数値に変換される
console.log(a === b); // false 文字列は数値に変換されない
```


# クラス
- ES6から導入された文法
## オブジェクトの復習　
- 関数をオブジェクトの値にすることができる
```javascript
const user = {
    name: 'Akihiro',
    greet: () => {
        console.log('Hello!');
    }
};
// 関数呼び出し
user.greet();
```

## クラスの基本
- クラス名は大文字にする
```javascript
class Animal{
} // ←　セミコロンは不要

// animalをAnimalインスタンスと呼ぶ（クラスから生成したオブジェクトを特別にインスタンスと呼ぶ）
const animal = new Animal();
```

- コンストラクタ
    - インスタンスを生成したときに実行したい処理や設定を追加するための機能
    - this.プロパティ = 値;　の形でインスタンスにプロパティと値を追加できる
```javascript
class Animal {
    constructor(name, age){
        console.log('Hello World!');
        this.name = name;
        this.age = age;
    }
    greet(){
        console.log(`Hello ${this.name}!`);
    }

    info(){
        this.greet();
    }
}

const animal = new Animal('monkey');
// プロパティの値へアクセスする方法
console.log(animal.name); // 'monkey'
animal.greet(); // 'Hello monkey!'
animal.info(); // 'Hello monkey!'
```



# 継承
```javascript
class Dog extends Animal {

    constructor(name, age, breed){
        // 親クラスのコンストラクタを呼び出す
        super('monkey', 7);
        // 子クラス独自の処理を実行
        this.breed = breed;
    }

    getHumanAge() {
        return this.age * 7;
    }
    
    info(){
        this.greet();

        // オーバーライド
        const humanAge = this.getHumanAge();
        console.log(`${humanAge}歳です`);

        console.log(`犬種は${this.breed}です`);
    }
}

const dog = new Animal('Pochi', 7, 'チワワ');
dog.info(); // 'Hello Pochi!'

```




# ファイル分割
```javascript
// animal.js
class Animal {

}
// エクスポート(「デフォルトエキスポート」)
export default Animal;

// dog.js
// ファイル読み込み
import Animal from './animal';
class Dog extends Animal {

}
export default Dog;


// script.js
import Dog from './dog';

```
- エキスポート、インポートできるのはクラスだけでなく、文字列や数値や関数も可能。
```javascript
// sample1.js
const text = 'Hello World';
export default text;

// sample2.js
import text from './sample1';
console.log(text);
```
- デフォルトエキスポートは1ファイル1つの値のみ使える。exportで記述した値名とimportで記述した値名が異なっても問題ない。
- 複数の値をエキスポートしたい場合は、「名前付きエキスポート」を用いる
```javascript
// animal.js
class Animal {

}
const animal = new Animal();

// エクスポート(「デフォルトエキスポート」)
export { animal };

// dog.js
// ファイル読み込み
import { animal } from './animal';
class Dog extends Animal {

}
const dog1 = new Dog();
const dog2 = new Dog();
// 複数の値をエキスポートできる
export { dog1, dog2 };


// script.js
// 複数の値をインポートできる
import { dog1, dog2 } from './dog';

```


