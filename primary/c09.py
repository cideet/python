# 面向对象
# 有意义的面向对象，类并不等于真正的面向对象

# 类的定义
class Students():
    name = '张三丰'
    age = 0

    def print_file(self):
        return self.name


student = Students()  # 类的实例化
print(student.print_file())  # 类的调用
