# 面向对象
# 有意义的面向对象，类并不等于真正的面向对象

# 类的定义
class Students00():
    name = '张0丰'
    age = 0

    def print_file(self):
        return self.name


student00 = Students00()  # 类的实例化
print(student00.print_file())  # 类的调用

print('------------------------------------------------------------------------------')

# 单独的模块存放类，以下是调用方法
from c09_01_Students import Students11

student11 = Students11()
print(student11.print_file())

# 类是现实世界或思维世界中的实体在计算机中的反映，它将数据以及操作封装在一起
# 类是抽象的，实例化才叫对象
# 类可以比作印钞机的模板，实例化的少叫钞票

stu1 = Students11()
stu2 = Students11()
stu3 = Students11()
print(id(stu1), id(stu2), id(stu3))

print('------------------------------------------------------------------------------')


class Students22():
    name = '张2丰'
    age = 0

    def __init__(self):  # 构造函数，自动执行调用
        print('Students22->__init__')

    def print_file(self):
        return self.name


student22 = Students22()
print(student22.print_file())
# print(student22.__init__())  # __init__也可调用，因为没有return所以返回None

print('------------------------------------------------------------------------------')


class Students33():
    # 抽象的类，有实际的属性值，是不合适的
    name = '张3丰'  # 类变量

    def __init__(self, name, age):  # 初始化对象的属性 self可以改成任意单词，比如this
        self.name = name  # 实例变量
        self.age = age
        # self代表当前调用的对象，只和实例有关，与类无关。

    def print_file(self):
        return self.name, self.age


student33 = Students33('张三丰', 30)
print(student33.print_file())
print(Students33.name)  # 类变量
print(student33.__dict__)  # {'name':'张三丰','age':30}
print(Students33.__dict__)

print('------------------------------------------------------------------------------')

print('类变量')


class Students44():
    sum = 0  # 比如用作统计班级人数

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.sum += 1
        print(self.__class__.sum)


stu41 = Students44('张4丰1', 25)
stu42 = Students44('张4丰2', 26)
stu43 = Students44('张4丰3', 27)
print('此示例可以看出，类的每一次实例化，类变量sum+1')

print('------------------------------------------------------------------------------')

print('类方法和静态方法的定义和调用')


class Students55():
    sum = 0
    example = '示例类变量'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_file(self):  # 实例方法
        return self.name, self.age

    @classmethod  # 装饰器 类方法
    def plus_sum(cls):
        cls.sum += 17
        print(cls.sum)

    @staticmethod  # 静态方法
    def add(x, y):
        print(x + y)

    @staticmethod
    def add2(x, y):
        print(x + y)
        print('静态方法调用类变量', Students55.example)
        print('静态方法无法调用实例变量')


# st51 = Students55('张5丰11', 28)
Students55.plus_sum()  # 类方法的调用
# st52 = Students55('张5丰22', 29)
Students55.plus_sum()
st53 = Students55('张5丰33', 30)
st53.plus_sum()  # 实例对象也可以调用类方法，但不建议这么做
st53.add(55, 22)  # 静态方法的调用
Students55.add(22, 33)  # 静态方法的调用
st53.add2(31, 5)

print('------------------------------------------------------------------------------')


class Students66():
    def __init__(self):
        self.score = 0

    def marking(self, name, score):
        self.name = name
        self.score = score
        if self.score < 0:
            print('不能设置负分')
            return
        elif self.score > 100:
            print('不能超过100分')
            return
        print(self.name + '同学本次考试得分是：' + str(self.score) + '分')


stu6 = Students66()
# print('请给石敢当同学打分')
# score = int(input())
stu6.marking('石敢当', 78)

print('------------------------------------------------------------------------------')

print('私有方法')


class Students77():
    def __init__(self):
        self.score = 0

    def __marking(self, name, score):
        self.name = name
        self.score = score
        print(self.name + '同学本次考试得分是：' + str(self.score) + '分')


stu7 = Students77()
# stu7.__marking('石敢当', 77)
print('私有方法不能被调用')

print('------------------------------------------------------------------------------')

print('私有属性')


class Students88():
    def __init__(self):
        self.__score = 0
        self.height = '177cm'


stu8 = Students88()
stu8.__score = 65
print(stu8.__score)
print('不是类的私有属性能被实例对象赋值和读取，此处的__score只是实例对象动态添加的一个属性')
stu8.__rrr = 77
print(stu8.__rrr)
print('信了吗？')
stu88 = Students88()
# print(stu88.__score)  # 报错，私有属性不能被读取
print(stu88.height)
print('看懂了么？')
print(stu8.__dict__)
print(stu88.__dict__)
print('Python类的私有变量处理方式，让人很呵呵哇')

print('------------------------------------------------------------------------------')

from c09_human import Human


class Students99(Human):
    pass


print(Students99.sum)  # 访问到父类的属性
stu99 = Students99('石敢当', 30)
print(stu99.name, stu99.age)  # 读取到父类的属性
stu99.getInfo()  # 调用父类的方法

print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
