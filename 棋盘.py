# 小蓝拥有×大小的棋盘，一开始棋盘上全都是白子。小蓝进行了
# 次操作，每次操作会将棋盘上某个范围内的所有棋子的颜色取反
# (也就是白色棋子变为黑色，黑色棋子变为白色)。请输出所有操作
# 做完后棋盘上每个棋子的颜色。
# 输入格式
# 输入的第一行包含两个整数几，m,用一个空格分隔，表示棋盘大小
# 与操作数。
# 接下来m行每行包含四个整数x1,y1,x2,y2,相邻整数之间使用
# 一个空格分隔，表示将在x1至x2行和y1至y2列中的棋子颜色取
# 反。
# 输出格式
# 输出几行，每行个0或1表示该位置棋子的颜色。如果是白色则
# 输出0，否则输出1。
# 这段代码会超时，下面使用差分方法进行优化
# n,m = map(int,input().split())
# chessboard = [[0]*n for _ in range(n)]
# for _ in range(m):
#   x1,y1,x2,y2 = map(int,input().split())
#   for i in range(x1-1,x2):
#     for j in range(y1-1,y2):
#       chessboard[i][j] = 1 - chessboard[i][j]
# for row in chessboard:
#     print(''.join(map(str, row)))
n, m = map(int, input().split())
# 初始化一个全为0的(n + 1) x (n + 1)的二维数组来表示差分数组
diff = [[0] * (n + 2) for _ in range(n + 2)]
# 执行m次操作
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 更新差分数组的操作范围
    diff[x1][y1] += 1
    diff[x1][min(y2 + 1, n + 1)] -= 1
    diff[min(x2 + 1, n + 1)][y1] -= 1
    diff[min(x2 + 1, n + 1)][min(y2 + 1, n + 1)] += 1
# 计算最终棋盘状态
for i in range(1, n + 1):
    for j in range(1, n + 1):
        diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
        # 棋盘上该位置为偶数时为0，奇数时为1
        print(1 if diff[i][j] % 2 == 1 else 0, end='')
    print()