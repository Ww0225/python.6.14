# 编写一个算法来判断一个数n
# 是不是快乐数。
# 「快乐数」 定义为：
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为1，也可能是无限循环但始终变不到1。
# 如果这个过程结果为1，那么这个数就是快乐数。
# 如果n是快乐数就返回true ；不是，则返回false 。
# 示例1：
# 输入：n = 19
# 输出：true
# 解释：
# 1**2 + 9**2 = 82
# 8**2 + 2**2 = 68
# 6**2 + 8**2 = 100
# 1**2 + 0**2 + 0**2 = 1
class Solution:
    def getNext(self,num):
        happy_num = 0
        while num:
            happy_num += (num%10)**2
            num //= 10
        return happy_num
    def isHappy(self, n: int) -> bool:
        mid = set()
        while True:
            n = self.getNext(n)
            if n == 1:
                return True
            if n in mid:
                return False
            else:
                mid.add(n)