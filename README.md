# python

# 全面系统 Python3入门+进阶课程
# 从基础语法开始，体验python语言之美
https://coding.imooc.com/class/chapter/136.html#Anchor

Pycharm
https://download.jetbrains.8686c.com/python/pycharm-professional-2018.3.2.exe
https://blog.csdn.net/l15031138244/article/details/84927835

https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64-webinstall.exe

官方英文手册 https://docs.python.org/3/
廖学峰手册 https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000

IDLE

Python基本数据类型
Number (init float)
2进制 0b111 ==> 7 
8进制 0o777 ==> 511
16进制 0xff ==> 255
int(True) ==> 1
int(False) ==> 0
bool(66) ==> True
bool(0b0) ==> False
bool([]) ==> False
bool({}) ==> False
bool(None) ==> False

整除 9//7 ==> 1
print(r'\n12') ==> 'n12'
'hello'*3 ==> 'hellohellohello'
'world'[2] ==> 'r'
'world'[-2] ==> 'l'
截取前3个字符 'world'[0:3] ==> 'wor'
'hello world'[0:-3] ==> 'hello wo'
'hello world'[2:] ==> 'llo world' 截取第Index位到last
'hello world'[-5:] ==> 'world' 截取最后几位

type([123,444]) ==> class 'list'
["123","456"]+["789"] ==> ['123', '456', '789']
['123', '456', '789']*3 ==> ['123', '456', '789', '123', '456', '789', '123', '456', '789']

元组 (1,2,3)[2] ==> 3
(1,2,3)*3 ==> (1, 2, 3, 1, 2, 3, 1, 2, 3) 

int float bool str list tuple set dict
str list tuple 序列 序号 切片

3 in [1,2,4] 
4 not in (1,2,3)
len([1,2,3,4]) ==> 4
max('abc') ==> c
获取ascll码：ord('d') ==> 100

定义空集 set()
type({12,3}) ==》<class 'set'> 无序 元素不重复
len({1,2,3}) ==》3
1 in {1,2,3} ==》True
差集 {1,2,3,4,5,6}-{5,3} ==》{1, 2, 4, 6}
交集 {1,2,3,4,5,6}&{3,6} ==》{3, 6}
合集 {1,2,3,4,5,6}|{3,6,7} ==》{1, 2, 3, 4, 5, 6, 7}

定义字典dict {'A':'AAA','B':'BBB','C':'CCC'}
{'A':'AAA','B':'BBB'}['A'] ==> 'AAA'

身份运算符【is】（内存地址）
1==1.0 ==> True
1 is 1.0 ==> False
[1,2]==[1,2] ==》True
[1,2] is [1,2] ==> False 内存地址不同
{1,2,3}=={2,1,3} ==> True

type(11)==int
isinstance(111,int) ==> True
isinstance('11',(float,int)) ==> False

位运算符（把数字当作二进制数进行运算）
&按位与  |按位或  ^按位异或  -按位取反  <<左移  >>右移动

3 or 4 and 5 ==》3
(3 or 4)and 5 ==》5

进入目录，执行命令【python 6.1.py】
