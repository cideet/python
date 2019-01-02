# 匿名函数
def add11(x, y):
    return (x + y)


print(add11(4, 5))

print('此为匿名函数？？')
f = lambda x, y: x + y
print(f(4, 55))

print('------------------------------------------------------------------------------')

print('三元表达式')
x = 2
y = 3
r = x if x > y else y
print(r)

print('------------------------------------------------------------------------------')

print('map')

list_x = [1, 2, 3, 4, 5, 6, 7, 8]


def square(x):
    return x * x


# for x in list_x:
#     square(x)

r = map(square, list_x)
print(list(r))

print('----------------------- -------------------------------------------------------')

print('使用匿名函数优化代码')
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = map(lambda x: x * x, list_x)
print(list(list_y))

print('------------------------------------------------------------------------------')

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6, 7, 8]
r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))

print('------------------------------------------------------------------------------')

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6]
r = map(lambda x, y: x * x + y, list_x, list_y)
print(list(r))

print('------------------------------------------------------------------------------')

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
from functools import reduce

print('reduce连续计算')
r = reduce(lambda x, y: x + y, list_x)
print(r)
t = reduce(lambda x, y: x * y, list_x, 2)
print('reduce的初始值，比如上面表达式中的2')
print(t)

print('------------------------------------------------------------------------------')

list_x = [1, 2, 1, 2, 3, 1]
r = filter(lambda x: False if x == 1 else True, list_x)
print(list(r))
print('过滤掉list中值等于1的元素')

print('------------------------------------------------------------------------------')

# 装饰器
import time


def f4():
    print(int(time.time() * 1000))
    print('f4')


def f5():
    print(int(time.time() * 1000))
    print('f5')


f4()
f5()

print('------------------------------------------------------------------------------')


def print_current_time(func):
    print(time.time())
    func and func()


def f33():
    print('f33')


def f44():
    print('44')


print_current_time(f33)
print_current_time(f44)

print('------------------------------------------------------------------------------')

print('ES6的解决方案')


def decorator(func):
    def wrapper():
        print(time.time())
        func and func()

    return wrapper


def f1():
    print('f11111')


f = decorator(f1)
f1()

print('------------------------------------------------------------------------------')

print('装饰器的解决方案')


def decorator(func):
    def wrapper():
        print(time.time())
        func and func()

    return wrapper


@decorator
def f1():
    print('f222')


f1()

print('------------------------------------------------------------------------------')

print('如果带1个参数呢')


def decorator(func):
    def wrapper(name):
        print(time.time())
        func and func(name)

    return wrapper


@decorator
def f1(name):
    print('This is ' + name)


f1('如果带1个参数呢')

print('------------------------------------------------------------------------------')

print('如果带n个参数呢')


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func and func(*args, **kw)

    return wrapper


@decorator
def f444(name):
    print('This is ' + name)


@decorator
def f555(age, height):
    print(age)
    print(height)


f444('如果带1个参数呢')
f555(30, '177cm')

print('------------------------------------------------------------------------------')

print('关键字参数')


def f666(name, height, **kw):
    print(name, height, kw)


f666('张三丰', 177, a=1, b=2, c='123')  # 张三丰 177 {'a': 1, 'b': 2, 'c': '123'}

print('------------------------------------------------------------------------------')

print('关键字参数的装饰器')


@decorator
def f777(name, height, **kw):
    print(name, height, kw)


f777('张三丰', 177, a=1, b=2, c='123')

print('以上例子具体说明装饰器的作用，比如封装一个“打印当前时间”的装饰器，需要使用的函数就调用一下此装饰器。做到代码的复用')
print('装饰器不破坏代码的结构，又能实现代码的高度复用')
