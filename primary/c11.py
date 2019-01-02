print('Python的高级用法及语法')

print('------------------------------------------------------------------------------')

print('枚举类型Enum')

from enum import IntEnum  # 整型
from enum import Enum

# from enum import Enum,unique
# @unique # 装饰器，限制唯一
# class VIP(Enum):
# 枚举不能实例化，23种设计模式中的单例模式
# print('设计模式不是必须，设计模式的出现是为了解决代码频繁的改变。这不是一个人能解决的，需要团队的每一个成员对代码的质量有一个共同的认识。')

class VIP(Enum):
    YELLOW = 1  # 看似常量，实则变量
    GREEN = 2
    BLACk = 3
    RED = 4
    RED_ALIAS = 4

print(VIP.YELLOW)  # 打印出来的不是1，而是VIP.YELLOW
# VIP.YELLOW = 88  # Enum保护机制，修改就报错
print(VIP.RED.name, VIP.RED.value)  # RED 4
print(type(VIP.GREEN))  # <enum 'VIP'>
print(type(VIP.GREEN.value))  # <class 'int'>
print(VIP.GREEN == 2)  # False
print(VIP.GREEN.value == 2)  # True
for x in VIP:
    print(x)
    print(x.value)
for x in VIP.__members__.items():  # for x in VIP.__members__:
    print(x)
    print(x[1].value)

a = 1
print(VIP(a))  # VIP.YELLOW
print('将a=1转化为枚举类型，就可以进行下一步的运算了')

print('------------------------------------------------------------------------------')

# 业务逻辑的开发者，不考虑太多的封装性，基本不需要高阶知识
def curve_pre():
    a = 25
    def curve(x):
        return a * x * x
    return curve

f = curve_pre()
print(f(3))  # 225
print(f.__closure__[0].cell_contents)
print('闭包=函数+环境变量')

print('------------------------------------------------------------------------------')

origin = 0
def go(step):
    global origin
    print('----------global--------------')
    new_pos = origin + step
    origin = new_pos
    return origin
print(go(2))
print(go(3))
print(go(8))

print('------------------------------------------------------------------------------')

ori = 0
def factory(pos):
    def go(step):
        nonlocal pos
        print('-----------nonlocal------------')
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go

tourist = factory(ori)
print(tourist(2))
print(tourist(4))
print(tourist(7))

print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
