
# 通常の関数の実行方法
def morning():
    print('good morning')


morning()
# 関数を変数に代入して実行する
message = morning
message()

print('---------------------------------')
# 関数の引数として関数を使用する


def greet(func):
    func()


def morning():
    print('good morining')


def evening():
    print('good evening')


greet(morning)
greet(evening)
print('---------------------------------')


def list_check(num_list, threshold_val):
    after_num_list = []
    for num in num_list:
        if num >= threshold_val:
            after_num_list.append(num)
    return after_num_list


num_list = [-2, -1, 4, 2, -6, 0]
threshold_val = 2
result_list = list_check(num_list, threshold_val)
print(result_list)
print('---------------------------------')


def list_check(num_list, callback_func):
    after_num_list = []
    for num in num_list:
        if callback_func(num):
            after_num_list.append(num)
    return after_num_list


def callback_func1(num):
    if -1 <= num <= 1:
        return True
    else:
        return False


def callback_func2(num):
    if num % 2 == 0:
        return True
    else:
        return False


num_list = [-2, -1, 4, 2, -6, 0]
result_list1 = list_check(num_list, callback_func1)
print(result_list1)
result_list2 = list_check(num_list, callback_func2)
print(result_list2)
# コールバック関数を用意することの肝は、関数を拡張出来ること
# ここでいう、list_check関数を条件部分を「外部処理として定義」して、処理の一部として受け取り、関数を実行している
print('---------------------------------')


def list_check(num_list, callback_func):
    after_num_list = []
    for num in num_list:
        if callback_func(num):
            after_num_list.append(num)
    return after_num_list


num_list = [-2, -1, 4, 2, -6, 0]
# ラムダ式で引数となる関数を記載
result_list = list_check(num_list, lambda x: -1 <= x <= 1)
print(result_list)


print('---------------------------------')
