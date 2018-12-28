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

print('------------------------------------------------------------------------------')

str22 = 'abc,acc,agc,afc,aic'
# print(re.findall('a[(f)(c)]c', str22))
print("找出字符串中所有的afc或acc", re.findall('a[fc]c', str22))
print("这里可以理解为：两边的a和c是定界符，只是为了找出中间的内容f或c")
print("^非", re.findall('a[^fc]c', str22))
print(re.findall('[a-z]{3}', str22))

str33 = 'python12123php234java'
print(re.findall('[a-z]{3,6}', str33))  # ['python', 'php', 'java']
print('Python默认为贪婪规则，尽可能的匹配更多')
print('加?号将正则改成非贪婪模式')
print(re.findall('[a-z]{3,6}?', str33))  # ['pyt', 'hon', 'php', 'jav']

print('------------------------------------------------------------------------------')

str44 = 'pytho23213python35pythonn'
print(re.findall('python*', str44))  # ['pytho', 'python', 'pythonn']
print('*号表示匹配0次和无限多次')
print(re.findall('python+', str44))  # ['python', 'pythonn']
print('+号表示匹配1次和无限多次')
print(re.findall('python?', str44))  # ['pytho', 'python', 'python']
print('?号表示匹配0次和1次')
print(re.findall('python{1,2}', str44))
print(re.findall('python{1,2}?', str44))

str55 = 'pytho23213pythno35pythonn'
print(re.findall('python{1,2}', str55))
print(re.findall('python{1,2}?', str55))

print('------------------------------------------------------------------------------')

print('比如：正则匹配4-8位的QQ号')
# print('请输入QQ号')
# qq = input()
qq = '1234567'
res = re.findall('^[1-9]\d{3,7}$', qq)
if (len(res) > 0):
    print('QQ号输入正确', res[0])
else:
    print('QQ号匹配失败')

print('------------------------------------------------------------------------------')

str66 = 'PythonPythonPythonsdg'
reg = '(Python){3}'
print(re.findall(reg, str66))
print('某个正则表达式重复N次：(reg){n}')
print(re.findall('python', str66))
print('忽略大小写 re.I')
print(re.findall('python', str66, re.I))

print('------------------------------------------------------------------------------')

print('替换')
str77 = 'PHPPHPphpPHP124dPhpP'
newStr77 = re.sub('PHP', 'Python', str77)
newStr777 = re.sub('PHP', 'Python', str77, 1)  # 只替换一个
# re.sub('PHP', 'Python', str77)
print(str77)
print('字符串为什么没变？因为字符串类型是不可改变的')
print(newStr77)
print(newStr777)
print('替换中的忽略大小写呢？')

print('------------------------------------------------------------------------------')

print('re.sub中加入函数，将正则出的字符串动态替换')


def convert(value):
    # print(value)  # <_sre.SRE_Match object; span=(0, 3), match='PHP'>
    matched = value.group()
    return "!!" + matched + "!!"


str88 = 'PHPPHPphpPHP124dPhpP'
newstr = re.sub('PHP', convert, str88)
print(newstr)

print('------------------------------------------------------------------------------')

s = 'ABC3721D86'
print('找出数字，大于6换成9，小于6换成0')


def convert(value):
    matched = int(value.group())
    if (matched > 6):
        return '9'
    elif (matched < 6):
        return '0'
    else:
        return '6'


r = re.sub('\d', convert, s)
print(s + "==>>" + r)

print('------------------------------------------------------------------------------')

print('re.match-->>首字母开始匹配')
print('re.search-->>找第一个匹配')
print(re.match('a', 'abcdefg'))  # <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.match('b', 'abcdefg'))  # None
print(re.search('a', 'abcdefg'))  # <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.search('b', 'abcdefg'))  # <_sre.SRE_Match object; span=(1, 2), match='b'>
print(re.search('h', 'abcdefg'))  # None

print('------------------------------------------------------------------------------')

print('获取定界符之间的字符串（life和Python）')
s = 'life is short,I use Python'
print(re.search('life.*Python', s))
print('默认是一个分组，只是一般省略了()')
print(re.search('(life.*Python)', s))  # <_sre.SRE_Match object; span=(0, 26), match='life is short,I use Python'>
print(re.search('(life.*Python)', s).group())  # life is short,I use Python
print(re.search('(life.*Python)', s).group(0))  # life is short,I use Python
print(re.search('life(.*)Python', s).group(1))  # is short,I use
print('OK，就是我们想要的')
print(re.findall('life(.*)Python', s)[0])
print('看到没，findall优秀很多')

print('------------------------------------------------------------------------------')

s = 'life is short,I use Python, I love Python'
r = re.search('life(.*)Python(.*)Python', s)
print(r.group(0, 1, 2))  # ('life is short,I use Python, I love Python', ' is short,I use ', ', I love ')
print(r.groups())  # (' is short,I use ', ', I love ')

print('------------------------------------------------------------------------------')
