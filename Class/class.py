print('クラスの定義と使い方')


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
del person  # delete person object
print('------------------------------------------')
print('クラスの継承の方法')


class Car(object):
    def run(self):
        print('run')


class ToyotaCar(Car):  # Carクラスを継承している
    pass


class TeslaCar(Car):
    def auto_run(self):  # Carクラスを継承しつつ、auto_run()メソッドを追加している
        print('auto run')


car = Car()
car.run()
print('#################################')
toyota_car = ToyotaCar()
toyota_car.run()
print('#################################')
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

print('------------------------------------------')
print('メソッドの上書きと変数へのアクセス')


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):  # Carクラスを継承している
    def run(self):  # 継承したクラスのメソッドと同名のメソッド名で定義すると上書き出来る
        print('fast')


class TeslaCar(Car):
    def run(self):  # 継承したクラスのメソッドと同名のメソッド名で定義すると上書き出来る
        print('super fast')

    def auto_run(self):  # Carクラスを継承しつつ、auto_run()メソッドを追加している
        print('auto run')


car = Car()
car.run()
print('#################################')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)  # 　オブジェクト.変数名 で呼べる
toyota_car.run()
print('#################################')
tesla_car = TeslaCar('model S')
print(tesla_car.model)  # 　オブジェクト.変数名 で呼べる
tesla_car.run()
tesla_car.auto_run()

print('------------------------------------------')
print('親クラスのメソッドの呼び出し')


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):  # Carクラスを継承している
    def run(self):  # 継承したクラスのメソッドと同名のメソッド名で定義すると上書き出来る
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='model S', enable_auto_run=False):  # __init__()メソッドを上書きしたいが、
        # self.model = model# この部分が親クラスのコンストラクタと重複している =　無駄なコード

        # 親クラスのコンストラクタ部分を呼び出せる　⇛　「親クラスの要請」
        super().__init__(model)
        self.enable_auto_run = enable_auto_run  # TeslaCarクラスだけのクラス変数を定義
        # 親クラスに大量の__init__での設定値があり継承したいが、TeslaCarだけのクラス変数なども定義したい場合などに、
        # super().__init__()と書くことで対処できる

    def run(self):  # 継承したクラスのメソッドと同名のメソッド名で定義すると上書き出来る
        print('super fast')

    def auto_run(self):  # Carクラスを継承しつつ、auto_run()メソッドを追加している
        print('auto run')


car = Car()
car.run()
print('#################################')
toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)  # 　オブジェクト.変数名 で呼べる
toyota_car.run()
print('#################################')
tesla_car = TeslaCar('model S')
print(tesla_car.model)  # 　オブジェクト.変数名 で呼べる
tesla_car.run()
tesla_car.auto_run()

print('------------------------------------------')
print('プロパティを使った属性の設定')
# 勝手にenable_auto_runをTrueに書き換えられたくないとき


class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='model S', enable_auto_run=False):
        super().__init__(model)
        # self.__enable_auto_run = enable_auto_run # アンダーバー2つの場合は、クラス内であればアクセス可能になるが、一度オブジェクトを作るとアクセスは不可能になる
        self._enable_auto_run = enable_auto_run  # アンダースコア1つは、明示的に書き換えてほしくないときに使う

    @property
    def enable_auto_run(self):  # 読み込み可、書き込み不可
        return self._enable_auto_run

    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):  # 書き込み可にする
        self._enable_auto_run = is_enable

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar('model S')
tesla_car.enable_auto_run = True
print(tesla_car._enable_auto_run)

