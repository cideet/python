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
print('隔列取值')
for i in range(0, len(arr5), 2):
    print(arr5[i], end=' | ')
b5 = arr5[0:len(arr5):2]
print(b5)
print('arr5[0:len(arr5):2]')
print('通过序列的切片，实现隔列取值')
print('arr5[0:len(arr5):2]')
print('通过序列的切片，实现隔列取值')
