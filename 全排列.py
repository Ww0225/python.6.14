# 给定一个不含重复数字的数组nums ，返回其所有可能的全排列 。你可以按任意顺序返回答案。
# 示例1：
# 输入：nums = [1, 2, 3]
# 输出：[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = [0]*n

        def dfs(i,s):
            if i == n:
                ans.append(path.copy())
                return

            for x in s:
                path[i] = x
                dfs(i+1,s-{x})

        dfs(0,set(nums))
        return ans