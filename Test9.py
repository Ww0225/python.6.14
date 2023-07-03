import random
num = random.randint(1,100)
count = 0
guess_num = int(input("请输入你猜的数字:"))
while num != guess_num:
    print("猜错了")
    count += 1
    if guess_num > num:
        print("猜大了")
    else:
        print("猜小了")