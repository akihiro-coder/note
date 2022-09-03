class Person(object):
    def __init__(self, name):  # 「コンストラクタ」
        self.name = name
        print('First')
        print(self.name)

    def say_something(self):  # personが出来ることはクラス内にメソッドとして記述していくとまとまってわかりやすい
        print('hello')
        print('I am {}. hello'.format(self.name))  # 自分自身のクラス内の変数にアクセス可能
        self.run(3)  # クラス内で他のメソッドの内容を使うことが出来る

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('good bye')


person = Person('Mike')
person.say_something()
print('#################################')
