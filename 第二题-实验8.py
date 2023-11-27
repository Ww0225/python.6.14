# 编写程序：编写函数guess_fun模拟猜数游戏。
# 系统随机产生一个1-n（n为最大值，比如100）范围内整数，玩家进行猜测，
# 并设置猜测机会time（比如5次），系统在玩家猜测的过程中，
# 根据玩家测试的数据与系统生成的数进行对比，
# 并给予提示（比正确数字偏大或偏小了），玩家在机会范围内，
# 可以根据系统的提示对下一次的猜测进行适当的调整数值范围，以提高猜中的机率。
def guess_fun(n,time):
    import random
    num = random.randint(1,n+1)
    for i in range(time):
        x = int(input("请玩家输入一个数:"))
        if x > num:
            print(f"偏大了，次数剩余{time-i-1}次")
            continue
        elif x < num:
            print(f"偏小了，次数剩余{time-i-1}次")
            continue
        else:
            print(f"恭喜你猜中了，数字是:{num}")
            break

if __name__ == '__main__':
    n = int(input("请输入你要猜的数字的范围(1-n):"))
    times = int(input("请输入猜的次数:"))
    guess_fun(n,times)
