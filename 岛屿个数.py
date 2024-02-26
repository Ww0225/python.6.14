# 小蓝得到了一副大小为M×N的格子地图，可以将其视作一个只包
# 含字符'0'（代表海水）和'1'（代表陆地）的二维数组，地图之外可以
# 视作全部是海水，每个岛屿由在上下左右四个方向上相邻的'1'相连
# 接而形成。
# 在岛屿A所占据的格子中，如果可以从中选出k个不同的格子，使得
# 他们的坐标能够组成一个这样的排列：
# x0,0),(1,1),·,(ck-1,-1),其中
# (xi+1modk,y+1modk)是由（(xi,y)通过上下左右移动一次得来
# 的(0≤i≤k一1)，此时这k个格子就构成了一个“环”。如果另一
# 个岛屿B所占据的格子全部位于这个“环”内部，此时我们将岛屿B
# 视作是岛屿A的子岛屿。若B是A的子岛屿，C又是B的子岛
# 屿，那C也是A的子岛屿。
# 请问这个地图上共有多少个岛屿？在进行统计时不需要统计子岛屿的
# 数目。
# 输入格式
# 第一行一个整数T,表示有T组测试数据。
# 接下来输入T组数据。对于每组数据，第一行包含两个用空格分隔的
# 整数M、N表示地图大小；接下来输入M行，每行包含N个字
# 符，字符只可能是0或1'。
# 输出格式
# 对于每组数据，输出一行，包含一个整数表示答案。

from queue import Queue

switchOne = [(1,0),(0,1),(-1,0),(0,-1)]
switchTwo = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

# 通过 input() 获取输入的行数 m 和列数 n，并使用 split() 方法将其分割成两个整数。
# 创建一个二维列表 d，其大小为 (m+2) × (n+2)，并将其初始化为 0，这里在原始网格周围额外添加了一圈 0，目的是为了简化边界条件的处理。
# 循环读取每一行输入，将每一行的数字转换为整数并存储到二维列表 d 中。
# 最后返回这个二维列表 d。
def getData():
    m,n = map(int,input().split())
    data = [[0]*(n+2)]
    for i in range(m):
        line = [0] + [int(i) for i in input()] + [0]
        data.append(line)
    data.append([0]*(n+2))
    return data

# dfs() 函数实现了广度优先搜索算法，用于标记岛屿的所有相邻节点。其作用是：
# 接受参数 i 和 j 表示起始位置，data 表示网格的状态，visited 表示已经访问过的节点，size 表示队列的最大容量。
# 创建一个队列 q，并将起始位置加入队列。
# 循环直到队列为空，每次从队列中取出一个节点，并标记为已访问。
# 遍历该节点的四个相邻节点，如果相邻节点是陆地且未被访问过，则加入队列。
# 返回更新后的 visited 数组。
def dfs(i,j,data,visited,size):
    queue = Queue(maxsize=size)
    queue.put([i,j])
    while not queue.empty():
        node = queue.get()
        if visited[node[0],node[1]]:
            continue
        visited[node[0], node[1]] = 1
        for k in switchOne:
            tmp = [k[0] + node[0],k[1] + node[1]]
            if data[tmp[0]][tmp[1]] == 1 and visited[tmp[0]][tmp[1]] == 0:
                queue.put(tmp)
    return visited

# counter() 函数是主要的计算逻辑，用于计算岛屿的数量。其作用是：
# 接受一个二维列表 board 作为参数，表示网格的状态。
# 计算网格的行数 m 和列数 n，以及网格大小 size。
# 创建一个大小为 m × n 的 visited 数组，用于记录节点是否被访问过，并初始化 ans 为 0，用于记录岛屿的数量。
# 创建一个队列 queue1，并将起始位置 [0,0] 加入队列。
# 循环直到队列为空，每次从队列中取出一个节点 cur，并检查其是否已被访问过。
# 如果当前节点是陆地，则调用 dfs() 函数标记该岛屿的所有节点，并将 ans 加一。
# 如果当前节点是水域，则将其标记为已访问，并将其相邻的节点加入队列中。
# 返回岛屿的数量。
def counter(board):
    m = len(board)
    n = len(board[0])
    size = m * n
    visited = [[0]*n for _ in range(m)]
    ans = 0
    queue1 = Queue(maxsize=size)
    queue1.put([0,0])
    while not queue1.empty():
        cur = queue1.get()
        if visited[cur[0]][cur[1]]:
            continue
        if board[cur[0]][cur[1]]:
            dfs(cur[0],cur[1],visited,size)
            ans += 1
            continue
        else:
            visited[cur[0]][cur[1]] = 1
        for i in switchTwo:
            new_i = cur[0] + i[0]
            new_j = cur[1] + i[1]
            if new_i > -1 and new_i < m and new_j > -1 and new_j < n:
                if visited[new_i][new_j]:
                    continue
                else:
                    queue1.put([new_i,new_j])
    return ans

T = int(input())
for _ in range(T):
    board = getData()
    print(counter(board))