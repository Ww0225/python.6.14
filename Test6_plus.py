heght = int(input("请输入您的身高（cm）："))
vip_level = int(input("请输入您的VIP等级(1-5):"))
if heght < 120:
    print("身高小于120cm，可以免费")
elif vip_level > 3:
    print("vip级别大于3，可以免费")
else:
    print("不好意思，条件都不满足，需要买票10元")
print("祝您游玩愉快！")