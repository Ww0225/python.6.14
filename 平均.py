# 问题描述
# 有一个长度为n的数组(n是10的倍数)，每个数a;都是区间
# [0,9】]中的整数。小明发现数组里每种数出现的次数不太平均，而更改
# 第i个数的代价为b;,他想更改若干个数的值使得这10种数出现的
# 次数相等（都等于），请问代价和最少为多少。
# 输入格式
# 输入的第一行包含一个正整数。
# 接下来n行，第i行包含两个整数a,b,用一个空格分隔。
# 输出格式
# 输出一行包含一个正整数表示答案。
n = int(input())
numbers = [[] for _ in range(10)]
for i in range(n):
    a,b = map(int,input().split())
    numbers[a].append(b)  
ans = 0
k = n // 10
for i in range(10):
    ls = sorted(numbers[i])
    ans += sum(ls[:-k])
print(ans)