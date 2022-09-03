list1 = [1, 2, 3, 4, 5]
# リスト要素を一つずつ取り出したい
# 組み込み関数iter()を使用してイテレータオブジェクトを取得する
it = iter(list1)

# イテレータオブジェクトは組み込み関数next()を使用すると、要素を一つずつ取り出すことが出来る
for i in range(5):
    print(next(it))  # 1,2,3,4,5
# 組み込み関数iter()を使用してイテレータオブジェクトを取得する
print('-----------------------------------------')

# 取り出す要素がなくなると、StopIteration例外を出力
# print(next(it))


print('-----------------------------------------')


for i in list1:
    print(i)


print('-----------------------------------------')


class SampleIterator(object):
    def __init__(self, num):
        self.num = num
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.num:
            raise StopIteration()

        ret = self.current
        self.current += 1
        return ret


si = SampleIterator(3)
for i in range(3):
    print(next(si))  # 0,1,2


print('-----------------------------------------')

r = range(3)
print(type(r))  # range type


print('__iter__' in dir(r))
print('__next__' in dir(r))


# イテレータ：データの流れを表現するオブジェクト
# 自身を戻り値とする__iter__メソッド、次の要素を返す__next__メソッドを持つ

# 反復可能オブジェクト：要素を一度に一つずつ返せるオブジェクト
# それが内包イテレータを返す__iter__メソッドを持つ


print('-----------------------------------------')


a = iter([1, 2, 3, 4, 5])
print('__iter__' in dir(a))
print('__next__' in dir(a))
# __iter__()を実装しているオブジェクトは「イテラブル」と呼ぶ
# リストはイテラブルであり、イテレータではない


b = [1, 2, 3, 4, 5]
print('__iter__' in dir(b))
print('__next__' in dir(b))
# __next__()を実装しているオブジェクトは「イテレータ」と呼ぶ。
# イテレータは__iter__()を持つから、必ずイテラブルである


for i in a:
    print(i)

for i in b:
    print(i)
print('-----------------------------------------')


a = [1, 2, 3]
b = iter(a)
print(next(b))
print(next(b))
print(next(b))


print('-----------------------------------------')


l = [1, 2, 3]
it = iter(l)
# print(type(l))
# print(type(it))
# print(list(it))

print(next(it))
print(next(it))
print(next(it))

for i in l:
    print(i)
    print(l)


print('-----------------------------------------')


class Team:
    def __init__(self):
        self._member_list = []


team = Team()
team._member_list.extend(['アンパンマン', 'バイキンマン', 'ジャムおじさん'])
for member in team._member_list:  # 毎回書くのには長い
    print(member)

print('-----------------------------------------')
# 以下のように書き換える


class Team:
    def __init__(self):
        self._member_list = []

    def __iter__(self):
        return iter(self._member_list)


team = Team()
team._member_list.extend(['アンパンマン', 'バイキンマン', 'ジャムおじさん'])
for member in team:
    print(member)

# このようにfor文のinに書き込めるインスタンスオブジェクトまたはクラスのことを「イテラブル」と呼ぶ
print('-----------------------------------------')



