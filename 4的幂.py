class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n and n%4==0:
            n //= 4
        return n==1