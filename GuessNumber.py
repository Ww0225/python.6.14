import random
num = random.randint(1,10)
guess_num = int(input("第一次猜数字:"))
if  guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    guess_num = int(input("再一次猜数字:"))
    if guess_num == num:
        print("恭喜，第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
        guess_num = int(input("再一次猜数字:"))
        if guess_num == num:
            print("恭喜，第三次就猜中了")
        else:
            print("三次机会用完了，没有猜中")
