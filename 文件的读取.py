file1 = open("D:\py测试.txt","r",encoding="UTF-8")
# print(type(file1))
#
# print(file1.read())
#
# file1.close()
with open("D:\py测试.txt","r",encoding="UTF-8") as f:
    print(file1.read())