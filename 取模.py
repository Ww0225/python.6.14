# 问题描述
# 给定几，m,问是否存在两个不同的数x,y使得1≤x<y≤m且
# n mod x =n mod y.
# 输入格式
# 输入包含多组独立的涧问。
# 第一行包含一个整数T表示询问的组数。
# 接下来T行每行包含两个整数，m,用一个空格分隔，表示一组间
# 问。
# 输出格式
# 输出T行，每行依次对应一组间问的结果。如果存在，输出单词Ys:
# 如果不存在，输出单词No。
times = int(input())  # 输入测试次数
for _ in range(times):  # 对每组测试数据进行处理
    n, m = map(int, input().split())  # 获取当前测试数据的n和m
    flag = True  # 设定一个标志，初始值为True

    for y in range(1, m + 1):  # 遍历y范围为[1, m]
        if not flag:  # 如果flag已经变为False，跳出当前循环
            break
        for x in range(1, y):  # 对于x范围为[1, y)，遍历x
            if n % x == n % y:  # 检查是否存在n % x等于n % y的情况
                flag = False  # 若存在相等的情况，将flag设置为False
                print('Yes')  # 输出'Yes'
                break  # 跳出当前循环

    if flag:  # 如果flag仍为True，说明没有找到满足条件的x和y
        print('No')  # 输出'No'