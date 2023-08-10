try:
    file = open("D:/pyabc.txt","r",encoding="UTF-8")
except:
    print("出现异常了，因为文件不存在，我用w模式去打开")
    file = open("D:/pyabc.txt","w",encoding="UTF-8")

try:
    print(name)
    # 1 / 0
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)

try:
    1 / 0
except Exception as e:
    print("出现异常了")
else:
    print("很高兴，没有异常")
finally:
    print("over")
