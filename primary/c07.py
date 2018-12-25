# 循环语句

# count = 1
# while True:
#     count += 1
#     print('死循环', count)

count = 0
while count < 10:
    count += 1
    print("正确的while循环", count)
else:
    print('EOF')

arr = ['apple', 'orange', 'banana', 'grape']
for x in arr:
    print('arr', x)

arr2 = [[1, 2, 3], ('a', 'b', 'c')]
for x in arr2:
    for y in x:
        print('arr2', y)
else:
    print('一般没怎么用else')

arr3 = [1, 2, 3, 4, 5]
for x in arr3:
    if x == 3:
        print('break', x)
        break
    print('arr3', x)

arr4 = [1, 2, 3, 4, 5]
for x in arr4:
    if x == 3:
        print('continue', x)
        continue
    print('arr4', x)

for x in range(0, 10):
    print('for(i=0;i<10;i++)的替代方案', x)

for x in range(0, 10, 2):
    print('设定步长', x)

for x in range(10, 0, -1):
    print('递减', x)

arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('间隔取值')
# 第一种方法
for i in range(0, len(arr5), 2):
    print(arr5[i], end=' | ')
# 第二种方法
b5 = arr5[0:len(arr5):2]
print(b5)
print('arr5[0:len(arr5):2]')
print('通过序列的切片，实现间隔取值')
print('arr5[0:len(arr5):2]')
print('通过序列的切片，实现间隔取值')

# 包 -> 文件夹
# 模块 -> py文件
# 类 ->
# 函数、变量 ->

# 区分不同包的同名模块，需要在模块的前面加上包的名字
# 比如 six.c4 seven.c4
# 这也就是命名空间

# Python是如何区分普通文件夹和Python的包呢？
# 有没有“__init__.py”，就算为空

import c07_test  # 在c07.py中导入c07_test.py
import c07_test2.test  # 导入不同包的模块
import c07_test2.test as t  # as
from c07_test3.test import a  # from import
from c07_test3 import test  # from import
from c07_test4.test import *  # from import
from c07_test5.test import *  # __all__控制*导出
from c07_test6.test import *

# from c07_test5.test import a5, b5, c5, d5

print(c07_test.a)
print(c07_test2.test.a)
print(t.a)
print(a)
print(test.a)
print(a4, b4, c4, d4)
print(a5, b5, c5)  # __all__控制了d5的导出
print(a6, b6, c6)

# import sys
# import datetime
# import io
# print(sys.path)
# 每个模块中，重复导入模块

# # 可以借助__init__.py来实现
# import c07_test7
# print(c07_test7.sys.path)
