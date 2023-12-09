# 互质数的个数
# 问题描述
# 给定a,b,求1≤x<ab中有多少个x与ab互质。由于答案可能
# 很大，你只需要输出答案对998244353取模的结果。
# 输入格式
# 输入一行包含两个整数分别表示α，b,用一个空格分隔。
# 输出格式
# 输出一行包含一个整数表示答案。
# 样例输入1
# 25
# 样例输出1
# 16
# 样例输入2
# 127

def euler_phi(n):
  result = n
  p = 2
  while p*p <= n:
    if n % p == 0:
      while n % p == 0:
        n //= p
      result -= result // p
    p += 1
  if n > 1:
    result -= result // n
  return result

a,b = map(int,input().split())
print(euler_phi(a**b)%998244353)
