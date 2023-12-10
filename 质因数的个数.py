# 问题描述
# 给定正整数，请问有多少个质数是n的约数。
# 输入格式
# 输入的第一行包含一个整数n。
# 输出格式
# 输出一个整数，表示几的质数约数个数。
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

n = int(input())
count = 0
for i in range(1,n+1):
    if n % i == 0 and is_prime(n):
        count += 1
print(count)