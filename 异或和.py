# 问题描述
# 给一棵含有n个结点的有根树，根结点为1，编号为i的点有点权α
# (i∈[1，n)。现在有两种操作，格式如下：
# 方
# ·1xy:该操作表示将点x的点权改为y。
# ·2x:该操作表示查询以结点x为根的子树内的所有点的点权的
# 异或和。
# 现有长度为的操作序列，请对于每个第二类操作给出正确的结果。
# 输入格式
# 输入的第一行包含两个正整数几，m,用一个空格分隔。
# 第二行包含n个整数a1,a2,·,an,相邻整数之间使用一个空格分
# 隔。
# 接下来n一1行，每行包含两个正整数u,vi,表示结点u和v之
# 间有一条边。
# 接下来m行，每行包含一个操作。
# 输出格式
# 输出若干行，每行对应一个查询操作的答案。
n,m = map(int,input().split())
value = list(map(int,input().split()))
value.index(0,0)
yihuo = []
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,input().split())
    a,b = min(a,b),max(a,b)
    tree[a].append(b)
for i in range(m):
    op = list(map(int,input().split()))
    if op[0] == 1:
        value[op[1]] = op[2]
    else:
        x = op[1]
        vis = [x]
        qfront = 0
        qend = 1
        while qfront != qend:
            if tree[vis[qfront]] != []:
                vis.extend(tree[vis[qfront]])
                qend += len(tree[vis[qfront]])
            qfront += 1
        ans = value[vis[0]]
        for i in range(1,len(vis)):
            ans ^= value[vis[i]]
        yihuo.append(ans)
for i in range(len(yihuo)):
    print(i)

