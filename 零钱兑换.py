# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1
# 你可以认为每种硬币的数量是无限的。
from functools import cache
from math import inf


# capacity : 背包容量
# w[i] : 第 i 个物品的体积
# v[i] : 第 i 个物品的价值
# 每种物品可以无限次重复选
# 返回：所选物品体积和不超过 capacity 的前提下，所能得到的最大价值和
def unbounded_knapsack(capacity: int, w: list[int], v: list[int]) -> int:
    n = len(w)

    @cache
    def dfs(i, c):
        if i < 0:
            return 0
        if c < w[i]:
            return dfs(i - 1, c)
        return max(dfs(i - 1, c), dfs(i, c - w[i]) + v[i])

    return dfs(n - 1, capacity)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)

        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        ans = f[n][amount]
        return ans if ans < inf else -1

        # @cache
        # def dfs(i,c):
        #     if i < 0:
        #         return 0 if c == 0 else inf
        #     if c < w[i]:
        #         return dfs(i-1,c)
        #     return min(dfs(i-1,c),dfs(i,c-coins[i])+1)

        # ans = dfs(n-1,amount)
        # return ans if ans < inf else -1