# 参考資料：
# - https://qiita.com/mtb_beta/items/d257519b018b8cd0cc2e

# 返り値を持たないメソッドでのデコレーターの例
def deco(func):  # デコレータの定義関数
    def wrapper(*args, **kwargs):  # デコレータの中身の定義
        print('--start--')
        func(*args, **kwargs)
        print('--end--')
    return wrapper

# @deco : デコレーターの定義関数で次の関数をデコレートする意味


@deco
def test():
    print('hello')


test()

# デコレータは既存関数の処理の前後に自分自身で処理を付け加えることができる
print('======================================')


# 返り値を持つメソッドでのデコレーターの例
def deco2(func):
    import os

    def wrapper(*args, **kwargs):
        res = '--start--' + os.linesep
        res += func(*args, **kwargs) + '!' + os.linesep  # デコレートするメソッドの返り値を加工する
        res += '--end--'
        return res
    return wrapper


@deco2
def test2():
    return 'hello'


result = test2()
print(result)

# TODO: 何かを生成するメソッドをデコレートする場合、生成された結果が返ってくるようにデコレータを書かなければなりません。

# デコレータは値を返すメソッドをデコレート可能なだけでなく、デコレートするメソッドの返り値を加工することが可能

print('======================================')


# 複数のデコレータを定義し、複数デコレートする例
# htmlファイルをpythonで書いた例
def deco_html(func):
    def wrapper(*args, **kwargs):
        res = '<html>'
        res = res + func(*args, **kwargs)
        res = res + '</html>'
        return res
    return wrapper


def deco_body(func):
    def wrapper(*args, **kwargs):
        res = '<body>'
        res = res + func(*args, **kwargs)
        res = res + '</body>'
        return res
    return wrapper


@deco_html
@deco_body
def test():
    return 'Hello Decorator'


print(test())

print('======================================')

# もっと簡潔した例
# デコレータに引数を渡す


def deco_tag(tag):
    def _deco_tag(func):
        def wrapper(*args, **kwargs):
            res = '<' + tag + '>'
            res = res + func(*args, **kwargs)
            res = res + '</' + tag + '>'
            return res
        return wrapper
    return _deco_tag


@deco_tag('html')
@deco_tag('body')
def test():
    return 'Hello Decorator!'


print(test())

print('======================================')

# 引数を持つメソッドをデコレートする


def deco_p(func):
    def wrapper(*args, **kwargs):
        res = '<p>'
        res = res + func(args[0], **kwargs)
        res = res + '</p>'
        return res
    return wrapper


@deco_p
def test(str):
    return str


print(test('Hello Decorator!'))
