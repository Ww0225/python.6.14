# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
# 并返回其长度。如果不存在符合条件的子数组，返回 0 。
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        ans = n+1
        left = s = 0
        for right,num in enumerate(nums):
            s += num
            while s >= target:
                ans = min(ans,right-left+1)
                s -= nums[left]
                left+=1
        return ans if ans <= n else 0