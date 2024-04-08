n, lens = map(int, input().split())
lst = []  # 存管道阀门位置，打开时刻
for i in range(n):
    l, s = map(int, input().split())
    lst.append([l, s])


def check(time):
    res = []  # 存每个阀门在规定时间内水流动的范围
    for l, s in lst:  # 取数据
        temp = time - s  # 当前时间减去开阀门的时刻
        if temp >= 0:  # 如果当前时间足以开阀门
            res.append([l - temp, l + temp])  # 记录当前阀门的水流动的范围
    res.sort(key=lambda x: x[0])  # 从小到大排序
    ans = res[0][1]  # 找到水流动最靠前的那个阀门的范围，取右界
    for i in range(1, len(res)):  # 从第 2 个阀门开始遍历
        if res[i][0] - ans <= 1:  # 如果第二个左界 - 第一个右界 <= 1，表明边界相连
            ans = max(ans, res[i][1])  # 更新 ans 并使其尽可能的大（使水流尽可能的覆盖更大的面积）
        else:  # 无法连接，有空隙，说明时间太少了
            break
    return ans >= lens  # 最后根据水流是否全覆盖来判断当前时间是否合规


left, right = 0, 10 ** 9
while left < right:
    mid = (left + right) // 2
    if check(mid):  # 如果符合时间要求，就继续寻找更短的时间
        right = mid
    else:  # 否则增加时间范围
        left = mid + 1
print(left)  # 输出结果