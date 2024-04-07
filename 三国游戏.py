# 问题描述
# 小蓝正在玩一款游戏。游戏中魏(X)、蜀(Y)、吴(Z)三个国家各自拥
# 有一定数量的士兵X,Y,Z(一开始可以认为都为0)。游戏有个
# 可能会发生的事件，每个事件之间相互独立且最多只会发生一次，当
# 第i个事件发生时会分别让X,Y,Z增加Ai,B,C。
# 当游戏结束时（所有事件的发生与否已经确定），如果X,Y,Z的其
# 中一个大于另外两个之和，我们认为其获胜。例如，当X>Y十Z
# 时，我们认为魏国获胜。小蓝想知道游戏结束时如果有其中一个国家
# 获胜，最多发生了多少个事件？如果不存在任何能让某国获胜的情况，
# 请输出一1。
# 输入格式
# 输入的第一行包含一个整数n。
# 第二行包含个整数表示A;,相邻整数之间使用一个空格分隔。
# 第三行包含个整数表示B;,相邻整数之间使用一个空格分隔。
# 第四行包含个整数表示C,相邻整数之间使用一个空格分隔。
# 输出格式
# 输出一行包含一个整数表示答案。
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
ans = 0
sum_x = 0
sum_y = 0
sum_z = 0
res_x = 0
res_y = 0
res_z = 0
new_x = sorted([a[i] - b[i] - c[i] for i in range(n)],reverse=True)
new_y = sorted([b[i] - a[i] - c[i] for i in range(n)],reverse=True)
new_z = sorted([c[i] - b[i] - a[i] for i in range(n)],reverse=True)
for i in range(n):
    sum_x += new_x[i]
    sum_y += new_y[i]
    sum_z += new_z[i]
    res_x = res_y = res_z = i + 1
    if sum_x > 0:
        ans = max(ans,res_x)
    if sum_y > 0:
        ans = max(ans,res_y)
    if sum_z > 0:
        ans = max(ans,res_z)
    if sum_x <= 0 and sum_y <= 0 and sum_z <= 0:
        break
print(ans if ans else -1)