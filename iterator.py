list_ = [1, 2, 3, 4, 5]
# リスト要素を一つずつ取り出したい
# 組み込み関数iter()を使用してイテレータオブジェクトを取得する
it = iter(list_)
# イテレータオブジェクトは組み込み関数next()を使用すると、要素を一つずつ取り出すことが出来る
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
print(next(it))  # 5
# 組み込み関数iter()を使用してイテレータオブジェクトを取得する
print('-----------------------------------------')
# 取り出す要素がなくなると、StopIteration例外を発生
# print(next(it))


print('-----------------------------------------')





