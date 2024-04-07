# 问题描述
# 给定n个数A,问能满足m!为∑(A;!)的因数的最大的m是多
# 少。其中m!表示m的阶乘，即1×2×3X···×m.
# 输入格式
# 输入的第一行包含一个整数n。
# 第二行包含个整数，分别表示A;,相邻整数之间使用一个空格分
# 隔。
# 输出格式
# 输出一行包含一个整数表示答案。
from collections import defaultdict
n = int(input())
nums = list(map(int,input().split()))
dict = defaultdict(int)
for i in nums:
    dict[i] += 1
m = nums[0]
while True:
    x = dict[0]
    if x % (m+1) == 0:
        dict[m+1] += x//(m+1)
        m += 1
    else:
        break
print(m)