# 编写函数计算任意位数的黑洞数。
# 黑洞数是指：有这一样一个整数，由这个整数每位数字出来重组成一个最大数，
# 再减去每位数字重组成的最小数，结果仍然是得到这个数本身。
# 比如，3位黑洞数495=954-459，4位黑洞数6174=7641-1467。
def black_num(n):
    for num in range(10**(n-1),10**n):
        sorted_str_nums = sorted(str(num))
        max_num = int(''.join(sorted_str_nums[::-1]))
        min_num = int(''.join(sorted_str_nums))
        if max_num - min_num == num:
            print(f"发现{n}黑洞数:{num} = {max_num} - {min_num}")
if __name__ == '__main__':
    n = int(input("请输入你要看的黑洞数的位数:"))
    black_num(n)