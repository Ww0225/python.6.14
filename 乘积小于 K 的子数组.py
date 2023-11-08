# 给你一个整数数组nums和一个整数k ，请你返回子数组内所有元素的乘积严格小于k的连续子数组的数目。
# 示例1：
# 输入：nums = [10, 5, 2, 6], k = 100
# 输出：8
# 解释：8个乘积小于100的子数组分别为：[10]、[5]、[2],、[6]、[10, 5]、[5, 2]、[2, 6]、[5, 2, 6]。
# 需要注意的是[10, 5, 2]并不是乘积小于100的子数组。
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        prod = 1
        ans = 0
        for right,num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[left]
                left+=1
            ans += right - left+1
        return ans