# 函数
print('内置函数')
print('round()取两位', round(1.28856, 2))


# import sys
# sys.setrecursionlimit(2000)  # 改变默认递归数


# 自定义函数
def add(x, y):
    return x + y


def print11(code):
    print(code)
    # 没有return的函数，默认返回None


print11(add(111, 222))

print(print11(111))


def damage(skill1, skill2):
    return skill1 * 2.5, skill2 * 5 + 30


# damages = damage(22, 33)
# print(damages[0])
# print(damages[1])
# 不建议这样使用返回值

ski1, skil2 = damage(33, 22)  # 序列解包
print(ski1)
print(skil2)

# a=1
# b=2
# c=3
# 不如写成
a, b, c = 1, 2, 3  # 序列解包
print(a, b, c)
