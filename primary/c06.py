print('请输入你的身高（cm）')
input_height = int(input())
if input_height <= 150:
    print('浓缩的才是精华')
elif input_height <= 170:
    print('你身高一般')
elif input_height > 190:
    print('长这么高干嘛')
else:
    print('你的正常身高')

account = 'zsf'
password = '123'
print('please input account')  # IDLE接收用户输入
input_account = input()
print('please input password')
input_password = input()
print('你输入了:', input_account, input_password)
if account == input_account and password == input_password:
    print('验证OK')
else:
    print('用户名或密码错误')

mood = True
if mood:
    print('IF判断111')
    print('IF判断11111')
else:
    print('IF判断222')

mood11 = False
if mood11:
    print('True')
    print('有缩进则显示不了')
print('无缩进则跳出逻辑')  # 此行显示，已跳出判断逻辑
