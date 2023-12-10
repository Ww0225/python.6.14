# 题目描述
# 对于一个行m列的表格，我们可以使用螺旋的方式给表格依次填
# 上正整数，我们称填好的表格为一个螺旋矩阵。
# 例如，一个4行5列的螺旋矩阵如下：
# 12345
# 141516176
# 132019187
# 12111098
# 输入描述
# 输入格式：
# 输入的第一行包含两个整数几，m,分别表示螺旋矩阵的行数和列数。
# 第二行包含两个整数，C,表示要求的行号和列号。
# 其中，2≤n,m≤1000,1≤r≤n,1≤c≤m.
# 输出描述
# 输出一个整数，表示螺旋矩阵中第？行第c列的元素的值。
# 读取输入的 n、m 以及指定的 r、c
n, m = map(int, input().split())  # 行数和列数
r, c = map(int, input().split())  # 指定位置的行号和列号

# 创建一个大小为 n 行 m 列的矩阵并初始化为 0
mat = [[0] * m for _ in range(n)]

# 初始化螺旋矩阵填充的边界指针
left, right, top, base = 0, m - 1, 0, n - 1

num = 1  # 从 1 开始填充矩阵的值
while num <= n * m:
    # 从左到右填充上方行
    for i in range(left, right + 1):
        mat[top][i] = num
        num += 1
    top += 1

    # 从上到下填充右侧列
    for i in range(top, base + 1):
        mat[i][right] = num
        num += 1
    right -= 1

    # 从右到左填充底部行
    for i in range(right, left - 1, -1):
        mat[base][i] = num
        num += 1
    base -= 1

    # 从下到上填充左侧列
    for i in range(base, top - 1, -1):
        mat[i][left] = num
        num += 1
    left += 1

# 输出指定位置(r, c)上的值，注意索引从0开始，所以需要减1
print(mat[r - 1][c - 1])