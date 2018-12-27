class Human():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getInfo(self):
        print(self.name + '今年' + str(self.age) + '岁')
