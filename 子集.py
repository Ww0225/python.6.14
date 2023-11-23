# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        n = len(nums)
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            # 不选
            dfs(i+1)
            #选
            path.append(nums[i])
            dfs(i+1)
            path.pop()

        dfs(0)
        return ans