# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        # 将数组中的非正整数和大于n的数替换为1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # 找到第一个正数对应的位置，即为缺失的最小正整数
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果数组中都是正整数，返回n+1
        return n + 1