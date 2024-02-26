# 问题描述
# 给定一个长度为N的整数数列：A1,A2,·.·,AN。你要重复以下操作K次：
# 每次选择数列中最小的整数（如果最小值不止一个，选择最靠前
# 的)，将其删除。并把与它相邻的整数加上被删除的数值。输出K次操作后的序列。
# 输入格式
# 第一行包含两个整数N和K。
# 第二行包含N个整数，A1,A2,A3,.·,AN。
# 输出格式
# 输出N一K个整数，中间用一个空格隔开，代表K次操作后的序列。
def min_operations(arr, k):
    # 定义函数 min_operations，接受整数序列 arr 和操作次数 k 作为参数
    n = len(arr)
    # 获取整数序列的长度并赋值给变量 n
    for _ in range(1,k):
        # 开始循环执行 K 次操作
        min_index = 0
        # 初始化最小值索引为 0
        for i in range(1,n):
            # 遍历整数序列中的每个元素（从索引 1 开始）
            if arr[i] < arr[min_index]:
                # 如果当前元素比最小值小
                i = min_index
                # 更新最小值索引为当前索引 i
        if min_index > 0:
            # 如果最小值索引大于 0，说明最小值有前一个相邻的整数
            arr[min_index - 1] += arr[min_index]
            # 将前一个相邻整数加上最小值
        if min_index < n - 1:
            # 如果最小值索引小于整数序列长度减 1，说明最小值有后一个相邻的整数
            arr[min_index + 1] += arr[min_index]
            # 将后一个相邻整数加上最小值
        arr.pop(min_index)
        # 删除最小值所在位置的元素
        n -= 1
        # 更新整数序列长度
    return arr
    # 返回经过 K 次操作后的整数序列

# 读取输入
n,k = map(int,input().split())
# 读取整数序列长度 n 和操作次数 k
arr = list(map(int,input().split()))
# 读取整数序列并转换为列表

# 进行操作并输出结果
result = min_operations(arr,k)
# 调用 min_operations 函数，对整数序列进行 K 次操作
print(*result)
# 输出 K 次操作后的整数序列，*result 将列表展开为多个参数并以空格分隔
