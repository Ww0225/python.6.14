try:
    a = int(input("请输入一个整数（被除数）:"))
    b = int(input("请输入一个整数（除数）:"))
    c = a / b
except ZeroDivisionError:
    print("除数不能为0")
except ValueError:
    print("不是整型数据")
else:
    print("您输入的两个数相除的结果是: ",c)
finally:
    print("程序结束！")
