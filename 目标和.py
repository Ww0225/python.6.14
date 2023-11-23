# 给你一个非负整数数组 nums 和一个整数 target 。
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
from functools import cache

# capacity : 背包容量
# w[i] : 第 i 个物品的体积
# v[i] : 第 i 个物品的价值
# 返回：所选物品体积和不超过 capacity 的前提下，所能得到的最大价值和
def zero_one_knapsack(capacity:int,w:list[int],v:list[int])->int:
    n = len(w)

    @cache
    def dfs(i,c):
        if i < 0:
            return 0
        if c < w[i]:
            return dfs(i-1,c)
        return max(dfs(i,c),dfs(i-1,c-w[i])+v[i])

    return dfs(n-1,capacity)

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # p 添加的正数的和
        # s-p 添加的负数的和
        # p-(s-p) = t
        # 2p = s+t
        # p = (s+t)/2
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2

        n = len(nums)
        f = [[0] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x]
        return f[n][target]

        # @cache
        # def dfs(i,c):
        #     if i < 0:
        #         return 1 if c == 0 else 0
        #     if c < nums[i]:
        #         return dfs(i-1,c)
        #     return dfs(i-1,c) + dfs(i-1,c-nums[i])
        #
        # return dfs(n-1,target)