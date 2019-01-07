print('用字典代替switch')

switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday'
}
day1 = 2
day2 = 9
# day_name = switcher[day1]
print(switcher.get(day1, 'Unkown'))
print(switcher.get(day2, 'Unkown'))

print('------------------------------------------------------------------------------')

print('用字典印射代替switch（执行函数）')


def get_sunday():
    return 'Sunday'


def get_monday():
    return 'Monday'


def get_tuesday():
    return 'Tuesday'


def get_default():
    return 'Unkown'


switcher2 = {
    0: get_sunday(),
    1: get_monday(),
    2: get_tuesday()
}
print(switcher2.get(1, get_default()))
print(switcher2.get(8, get_default()))

print('------------------------------------------------------------------------------')

print('列表推导式')

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i ** 2 for i in a]
c = [i ** 2 for i in a if i > 4]
print(a)
print(b)
print(c)
print('list可以，元组类型也可以')
d = {1, 2, 3, 4}
print({i ** 3 for i in d})

print('------------------------------------------------------------------------------')

print('字典交换key和value')

e = {'张': 11, '三': 22, '丰': 33}
print([key for key, value in e.items()])
print({value: key for key, value in e.items()})

print('------------------------------------------------------------------------------')

print(None == '')
print(None == False)
print(None == [])
print(type(None))  # NoneType
print('None表示不存在')

print('------------------------------------------------------------------------------')

print(bool(None))
print(bool([]))
print(bool('0'))

print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
