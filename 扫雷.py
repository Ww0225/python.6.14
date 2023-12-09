# 题目描述
# 在一个行m列的方格图上有一些位置有地雷，另外一些位置为
# 空。
# 请为每个空位置标一个整数，表示周围八个相邻的方格中有多少个地
# 雷。
# 输入描述
# 输入的第一行包含两个整数n,m。
# 第2行到第n+1行每行包含m个整数，相邻整数之间用一个空格
# 分隔。如果对应的整数为0，表示这一格没有地雷。如果对应的整数
# 为1，表示这一格有地雷。
# 其中，1≤n,m≤100分钟后还是在当天。
# 输出描述
# 输出n行，每行m个整数，相邻整数之间用空格分隔。
# 对于没有地雷的方格，输出这格周围的地雷数量。对于有地雷的方
# 格，输出9。
n,m = map(int,input().split())
dilei = []
for _ in range(n):
    dilei.append(list(map(int,input().split())))
res = [[0 for _ in range(m)] for _ in range(n)]
dir = [(-1,-1),(1,1),(-1,1),(1,-1),(1,0),(-1,0),(0,1),(0,-1)]
for i in range(n):
    for j in range(m):
        if dilei[i][j] == 1:
            res[i][j] = 9
            for x in dir:
                xi = i + x[0]
                xj = j + x[1]
                if 0 <= xi <= n-1 and 0 <= xj <= m-1:
                    if res[xi][xj] != 9:
                        res[xi][xj] += 1
for i in range(n):
    for j in range(m):
        print(res[i][j],end=' ')
    print()