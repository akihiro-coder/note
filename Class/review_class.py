

class Person():
    def __init__(self, name):
        self.name = name
        print('First')
        print(self.name)

    def say_something(self):
        print('hello')
        print(f'I am {self.name}. Hello.')

    def run(self, num):
        print('run' * num)

    def __del__(self):
        print('good bye.')


person = Person('Taro')
person.say_something()
person.run(10)

del person  # 明示的にオブジェクトを削除できる

print('================================================================================')

# クラスの継承


class Car():
    def run(self):
        print('run')


class ToyotaCar(Car):
    pass


class Teslacar(Car):
    def auto_run(self):  # クラスが継承しつつ、メソッドを追加している
        print('auto run')


car = Car()
car.run()
toyota_car = ToyotaCar()
toyota_car.run()  # クラスがCarクラスを継承　⇛　親クラスのメソッドがそのまま使える
tesla_car = Teslacar()
tesla_car.run()
tesla_car.auto_run()

print('================================================================================')

# メソッドの上書きと変数へのアクセス


class Car():
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):  # 親クラスと同名メソッドで上書き
        print('fast')


class TeslaCar(Car):
    def run(self):  # 親クラスと同名メソッドで上書き
        print('super fast')

    def auto_run(self):
        print('auto run')


car = Car()
car.run()
toyota_car = ToyotaCar()
toyota_car.run()
tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()

super_car = ToyotaCar(model='supra')
print(super_car.model)
electric_car = TeslaCar(model='model S')
print(electric_car.model)


print('================================================================================')


# 親クラスのメソッドの呼び出し


class Car():
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):  # 親クラスと同名メソッドで上書き
        print('fast')


class TeslaCar(Car):
    def __init__(self, model=None, enable_auto_run=False):
        # self.model = model # この部分が重複している
        super().__init__(model)  # 親クラスのコンストラクタを呼び出せる。
                            # 再び書きたくないクラス変数を__init__(クラス変数)と書いておけばいい
        self.enable_auto_run = enable_auto_run

    def run(self):  # 親クラスと同名メソッドで上書き
        print('super fast')

    def auto_run(self):
        print('auto run')



tesla_car = TeslaCar(model='model s', enable_auto_run=True)
print(tesla_car.model)
print(tesla_car.enable_auto_run)
