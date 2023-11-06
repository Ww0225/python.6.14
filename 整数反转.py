# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
# 如果反转后整数超过 32 位的有符号整数的范围 [−2**31,  2**31 − 1] ，就返回 0。
# 假设环境不允许存储 64 位整数（有符号或无符号）。
class Solution:
    def reverse(self, x: int) -> int:
        y,res = abs(x),0
        of = (1<<31)-1 if x>0 else 1<<31
        while y!=0:
            res = res*10+y%10
            if res>of:
                return 0
            y //= 10
        return res if x>0 else -res