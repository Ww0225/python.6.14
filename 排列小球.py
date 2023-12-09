# 题目描述
# 小蓝有黄绿蓝三种颜色的小球，分别为R,G,B个。同样颜色的小球
# 没有区别。
# 小蓝将这些小球从左到右排成一排，排完后，将最左边的连续同色小
# 球个数记为1，将接下来的连续小球个数记为2，以此类推直到最右
# 边的小球。
# 请问，总共有多少总摆放小球的方案，使得1，t2,··为严格单调递
# 增序列，即t1≤t2≤t3≤…。
# 输入描述
# 输入一行包含三个整数R,G,B。
# 其中，0<R,G,B<50。。
# 输出描述
# 输出一个整数，表示答案。
RGB = list(map(int,input().split()))
total = sum(RGB)
res = 0

def dfs(color,n,t):
    global res
    if n == total:
        res += 1
        return
    for i in range(3):
        if color == i and RGB[color] != 0:
            RGB[color] -= 1
            dfs(color,n+1,t+1)
            RGB[color] += 1
        else:
            if RGB[i] >= t+1:
                RGB[i] -= t+1
                dfs(i,n+t+1,t+1)
                RGB[i] += t+1

dfs(0,0,0)
print(res)