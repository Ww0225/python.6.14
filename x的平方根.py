# 给你一个非负整数 x ，计算并返回 x 的 算术平方根
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5

# 法一：使用math库下的sqrt()函数
# 法二：二分查找法
x = int(input())
left,right=0,x+1
while left<right:
    mid = (left+right)//2
    if mid**2 == x:
        print(mid)
        break
    elif mid**2 < x:
        left = mid+1
    else:
        right = mid