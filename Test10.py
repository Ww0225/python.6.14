import random
num = random.randint(1,100)
isFlag = True
count = 0
while isFlag:
    guess_num = int(input("请输入你猜测的数字："))
    if num == guess_num:
        print("猜中了")
        isFlag = False
    else:
        count += 1
        if num > guess_num:
            print("猜小了")
        else:
            print("猜大了")
print(f"你总共猜了{count}次")

