# 给你两个整数，被除数dividend和除数divisor。
# 将两数相除，要求不使用乘法、除法和取余运算。
# 整数除法应该向零截断，也就是截去（truncate）其小数部分。
# 例如，8.345将被截断为8 ，-2.7335将被截断至 - 2 。
# 返回被除数dividend除以除数divisor得到的商 。
# 注意：假设我们的环境只能存储32位有符号整数，其数值范围是[−2**31, 2**31 − 1] 。
# 本题中，如果商严格大于2**31 − 1 ，则返回2**31 − 1 ；如果商严格小于 - 2**31 ，则返回 - 2**31 。
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2*31 and divisor==-1:
            return 2**31-1
        a,b,res=abs(dividend),abs(divisor),0
        for i in range(31,-1,-1):
            if (b<<i)<=a:
                res += 1<<i
                a -= b<<i
        return res if (dividend>0) == (divisor) else -res
