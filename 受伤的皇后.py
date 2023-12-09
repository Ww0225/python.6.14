# 题目描述
# 有一个n×n的国际象棋棋盘(n行n列的方格图)，请在棋盘中
# 摆放个受伤的国际象棋皇后，要求：
# 1.任何两个皇后不在同一行。
# 2.任何两个皇后不在同一列。
# 3.如果两个皇后在同一条45度角的斜线上，这两个皇后之间行号的
# 差值至少为3。
# 请问一共有多少种摆放方案。
# 输入描述
# 输入的第一行包含一个整数n。
# 其中，1≤n≤10。
# 输出描述
# 输出一个整数，表示答案。
count = 0
def queen(A,n=0):
    global count
    if n == len(A):
        count += 1
        return
    for col in range(len(A)):
        A[n] = col
        flag = 1
        for row in range(n):
            if A[row] == col or (abs(col-A[row])==n-row and n-row<3):
                flag = 0
                break
        if flag == 1:
            queen(A,n+1)

queen([0]*int(input()))
print(count)