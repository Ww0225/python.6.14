# 问题描述
# 给定一棵包含n个结点的完全m叉树，结点按从根到叶、从左到右
# 的顺序依次编号。例如下图是一个拥有11个结点的完全3叉树。
# 10
# 你需要求出第k个结点对应的子树拥有的结点数量。
# 输入格式
# 输入包含多组询问。
# 输入的第一行包含一个整数T，表示询问次数。
# 接下来T行，每行包含三个整数n,m,k,表示一组询问。
# 输出格式
# 输出T行，每行包含一个整数表示对应询问的答案。
t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    l = k
    r = k
    ans = 1
    res = 1
    while r*m+1 <= n:
        res *= m
        l = l*m-m+2
        r = r*m+1
        ans += res
    l = l*m-m+2
    ans += max(0,m-l+1)
    print(ans)
