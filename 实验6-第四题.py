test = input("请输入你的用户名:")
password = "666666"
for i in range(3):
    in_password = input("请输入用户名密码:")
    if password == in_password:
        print("登录成功！")
        break
    elif i==3-1:
        print("3次用户名或者密码均有误！退出程序")
        break
    else:
        print("密码错误，请重新输入")