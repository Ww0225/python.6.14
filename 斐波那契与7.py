# 问题描述
# 斐波那契数列的递推公式为：Fm=Fn-1十Fn-2,其中F=F2=1
# 请问，斐波那契数列的第1至202202011200项（含）中，有多少项的个
# 位是7。
def count_sevens_in_fibonacci():
    # 计算斐波那契数列的个位数，存储在数组中
    fib = [0]*60
    fib[0] = 0
    fib[1] = 1
    for i in range(2,60):
      fib[i] = (fib[i-1]+fib[i-2]) % 10

    # 统计周期内个位数为7的数量
    count_sevens = sum(1 for num in fib[:60] if num == 7)

    # 计算完整周期的个位数为7的数量
    full_cycles = 202202011200 // 60
    total_sevens = full_cycles * count_sevens

    # 计算剩余部分中个位数为7的数量
    remaining = 202202011200 % 60
    total_sevens += sum(1 for num in fib[:remaining] if num == 7)

    return total_sevens

result = count_sevens_in_fibonacci()
print(result)

