# 正则表达式是一个特殊的字符序列

program = 'C|C++|Java|C#|Python|JavaScript'
print(program.index('Python'))  # 14
print('Python' in program)  # True

import re

# re.findall('正则表达式', '字符串')
program = 'C|C++|Java|C#|Python|JavaScript'
print(re.findall('Python', program))  # ['Python']
print(re.findall('python', program))  # []
print(re.findall('C', program))  # ['C', 'C', 'C']
print(len(re.findall('C', program)))  # 3
print('常量正则表达式，看着无聊不无聊？')

str11 = '1234sdf43 dsd^g4gfg'
print('正则出所有数字')
print(re.findall('\d', str11))  # ['1', '2', '3', '4', '4', '3', '4']
print('正则出所有非数字')
print(re.findall('\D', str11))  # ['s', 'd', 'f', 'd', 's', 'd', 'g', 'g', 'f', 'g']
print('\d叫元字符')
print('正则出数字和字母')
print(re.findall('\w', str11))
print(re.findall('\W', str11))  # [' ', '^']
print(re.findall('\s', str11))  # 匹配空白字符

str22 = 'abc,acc,agc,afc,aic'
# print(re.findall('a[(f)(c)]c', str22))
print("找出字符串中所有的afc或acc", re.findall('a[fc]c', str22))
print("^非", re.findall('a[^fc]c', str22))
print(re.findall('[a-z]{3}', str22))

str33 = 'python12123php234java'
print(re.findall('[a-z]{3,6}', str33))  # ['python', 'php', 'java']
print('Python默认为贪婪规则，尽可能的匹配更多')
print('加?号将正则改成非贪婪模式')
print(re.findall('[a-z]{3,6}?', str33))  # ['pyt', 'hon', 'php', 'jav']

str44 = 'pytho23213python35pythonn'
print(re.findall('python*', str44))  # ['pytho', 'python', 'pythonn']
print('*号表示匹配0次和无限多次')
print(re.findall('python+', str44))  # ['python', 'pythonn']
print('+号表示匹配1次和无限多次')
print(re.findall('python?', str44))  # ['pytho', 'python', 'python']
print('?号表示匹配0次和1次')
print(re.findall('python{1,2}', str44))
print(re.findall('python{1,2}?', str44))

str55 =  'pytho23213pythno35pythonn'
print(re.findall('python{1,2}', str55))
print(re.findall('python{1,2}?', str55))