
#16.函数使用进阶
#调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可。
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result

def add(x, y):
    return x + y


def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5))  # 15





def is_even(num):
    return num%2==0

def square(num):
    return num**2

test_list=[35, 12, 8, 99, 60, 52]
result_list=list(map(square,filter(is_even,test_list)))
print(result_list)


#Lambda函数
#匿名函数，lambda 函数只能有一行代码，代码中的表达式产生的运算结果就是这个匿名函数的返回值。
test_list = [35, 12, 8, 99, 60, 52]
result_list = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums)))
print(result_list)  # [144, 64, 3600, 2704]



#Python 中的函数是“一等函数”，函数是可以直接赋值给变量的
import functools
import operator

# 用一行代码实现计算阶乘的函数
fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

# 用一行代码实现判断素数的函数
is_prime = lambda x: all(map(lambda f: x % f, range(2, int(x ** 0.5) + 1)))

# 调用Lambda函数
print(fac(6))        # 720
print(is_prime(37))  # True



# 偏函数
# 偏函数是指固定函数的某些参数，生成一个新的函数
import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
int16 = functools.partial(int, base=16)

print(int('1001'))    # 1001

print(int2('1001'))   # 9
print(int8('1001'))   # 513
print(int16('1001'))  # 4097