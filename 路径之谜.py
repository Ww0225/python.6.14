n = int(input())
visited = [[0] * n for _ in range(n)]
rol = list(map(int, input().split()))
cow = list(map(int, input().split()))
tar = (sum(rol) + sum(cow)) // 2  # 目标步数。
dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
p = ""

def dfs(x, y, path, bu):
    global p
    visited[x][y] = 1
    rol[x] -= 1
    cow[y] -= 1
    if rol[x] == 0:
        for i in range(x):
            if rol[i] > 0:
                return
    if cow[y] == 0:
        for i in range(y):
            if cow[i] > 0:
                return
    if x == n - 1 and y == n - 1:
        if sum(rol) == 0 and sum(cow) == 0 and bu == tar:
            p = path
            return
        else:
            return
    for xq, yq in dirs:
        xi, yi = x + xq, y + yq
        if 0 <= xi < n and 0 <= yi < n and visited[xi][yi] != 1 and rol[xi] > 0 and cow[yi] > 0:
            dfs(xi, yi, path + "/" + str(xi * n + yi), bu + 1)
            visited[xi][yi] = 0  # 回溯，
            rol[xi] += 1
            cow[yi] += 1

dfs(0, 0, "0", 1)
for i in p.split("/"):
    print(i, end=" ")