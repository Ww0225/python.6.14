# 小蓝负责花园的灌溉工作。
# 花园可以看成一个n行m列的方格图形。中间有一部分位置上安装
# 有出水管。
# 小蓝可以控制一个按钮同时打开所有的出水管，打开时，有出水管的
# 位置可以被认为已经灌溉好。
# 每经过一分钟，水就会向四面扩展一个方格，被扩展到的方格可以被
# 认为已经灌溉好。即如果前一分钟某一个方格被灌溉好，则下一分钟
# 它上下左右的四个方格也被灌溉好。
# 给定花园水管的位置，请问飞分钟后，有多少个方格被灌溉好？
# 输入描述
# 输入的第一行包含两个整数n,m。
# 第二行包含一个整数，表示出水管的数量。
# 接下来t行描述出水管的位置，其中第i行包含两个数r，c表示第r行第c列有一个排水管。
# 接下来一行包含一个整数k。
# 其中，1≤m,m≤100,1≤t≤10,1≤k≤100.
# 输出描述
# 输出一个整数，表示答案。
n,m = map(int,input().split())
t = int(input())
init = [[0 for _ in range(m)] for _ in range(n)]
after_water = [[0 for _ in range(m)] for _ in range(n)]
for i in range(t):
    r,c = map(int,input().split())
    init[r][c] = 1
k = int(input())
for _ in range(k):
    for i in range(n):
        for j in range(m):
            if init[i][j] == 1:
                after_water[i][j] = 1
            if i-1 >= 0:
                after_water[i-1][j] = 1
            if i+1 < n:
                after_water[i+1][j] = 1
            if j-1 >= 0:
                after_water[i][j-1] = 1
            if j+1 < n:
                after_water[i][j+1] = 1
    init = after_water
res = 0
for i in after_water:
    for j in i:
        res += j
print(res)