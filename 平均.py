# 有一个长度为n的数组(n是10的倍数)，每个数a;都是区间
# 0,91中的整数。小明发现数组里每种数出现的次数不太平均，而更改
# 第讠个数的代价为b;,他想更改若干个数的值使得这10种数出现的
# 次数相等（都等于），请问代价和最少为多少。
# 输入格式
# 输入的第一行包含一个正整数。
# 接下来n行，第i行包含两个整数a,b;，用一个空格分隔。
# 输出格式
# 输出一行包含一个正整数表示答案。
n = int(input())
nums_list = []
nums_dict = {}
for i in range(n):
    a,b = map(int,input().split())
    nums_list.append((a,b))
    if a in nums_dict.keys():
        nums_dict[a] += 1
    else:
        nums_dict[a] = 1
num = n / 10
sorted_nums = sorted(nums_list,key=lambda x:x[1])
value = 0
for i in range(n):
    a,b = sorted_nums[i]
    if nums_dict.get(a,0) > num:
        value += b
        nums_dict[a] -= 1
print(value)