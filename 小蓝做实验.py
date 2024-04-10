# 小蓝做实验
# 问题描述
# 小蓝很喜欢科研，他最近做了一个实验得到了一批实验数据，一共是两
# 百万个正整数。
# 如果按照预期，所有的实验数据x都应该满足107≤x≤108。
# 但是做实验都会有一些误差，会导致出现一些预期外的数据，这种误差
# 数据y的范围是103≤y≤1012。由于小蓝做实验很可靠，所以他
# 所有的实验数据中99.99%以上都是符合预期的。
# 小蓝的所有实验数据都在primes.txt中，现在他想统计这两百万个正
# 整数中有多少个是质数，你能告诉他吗？
txt = open(r'prime.txt','r',encoding='utf-8').read().split()
lst1 = [int(i) for i in txt if len(i) <= 8]
lst2 = [int(i) for i in txt if len(i) > 8]
res = [2]
ans = [True for _ in range(10**8+1)]
for i in range(2,10**8+1):
    if ans[i]:
        res.append(i)
    for j in range(i+i,10**8,i):
        ans[i] = False
count = 0
for i in lst1:
    if ans[i]:
        count += 1
for i in lst2:
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
        else:
            count += 1
print(1)