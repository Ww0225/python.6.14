# 问题描述
# 给定n个正整数Ai,请找出两个数i,j使得i<)且A;和A;存
# 在大于1的公因数。
# 如果存在多组i,j,请输出i最小的那组。如果仍然存在多组i,j,
# 请输出i最小的所有方案中了最小的那组。
# 输入格式
# 输入的第一行包含一个整数n。
# 第二行包含n个整数分别表示A1,A2,·.·,An,相邻整数之间使
# 用一个空格分隔。
# 输出格式
# 输出一行包含两个整数分别表示题目要求的i,),用一个空格分隔。
import math
def sieve_of_eratosthenes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2,int(math.sqrt(limit))+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i,limit+1,i):
                is_prime[j] = False
    return primes

n = int(input())
numbers = list(map(int,input().split()))
max_number = max(numbers)
primes = sieve_of_eratosthenes(max_number)
pos = [0] * (max_number+1)
ansi,ansj = n+1,-1
for i,x in enumerate(numbers,start=1):
    l = n+1
    for prime in primes:
        if prime > x:
            break
        if x % prime == 0:
            while x % prime == 0:
                x //= prime
            if pos[prime]:
                l = min(l,pos[prime])
            else:
                pos[prime] = i
    if x > 1:
        if pos[x]:
            l = min(l,pos[x])
        else:
            pos[x] = i
    if l < ansi:
        ansi = l
        ansj = i
print(ansi,ansj)