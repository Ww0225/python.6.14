# 小明非常不喜欢数字2，包括那些数位上包含数字2的数。如果一个
# 数的数位不包含数字2，小明将它称为洁净数。
# 请问在整数1至几中，洁净数有多少个？
# 输入描述
# 输入的第一行包含一个整数n(1≤n≤10)。
# 输出描述
# 输出一行包含一个整数，表示答案。

n = int(input())
print(sum([1 for i in range(1,n+1) if '2' not in str(i)]))