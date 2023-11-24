# 给你一个整数数组nums ，找到其中最长严格递增子序列的长度。
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3, 6, 2, 7]是数组[0, 3, 1, 6, 2, 2, 7]的子序列。

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        f = [0]*n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i],f[j])
            f[i] += 1
        return max(f)

        # @cache
        # def dfs(i):
        #     res = 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             res = max(res,dfs[j])
        #     return res + 1
        #
        # return max(dfs(i) for i in range(n))