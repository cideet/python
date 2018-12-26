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
