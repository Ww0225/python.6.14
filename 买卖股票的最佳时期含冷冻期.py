# 给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
from math import inf


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)

        f = [[0] * 2 for _ in range(n + 2)]
        f[1][1] = -inf
        for i, p in enumerate(prices):
            f[i + 2][0] = max(f[i + 1][0], f[i + 1][1] + p)
            f[i + 2][1] = max(f[i + 1][1], f[i][0] - p)
        return f[-1][0]

        # @cache
        # def dfs(i,hold):
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i-1,True),dfs(i-2,False) - prices[i])
        #     return max(dfs(i-1,False),dfs(i-1,True) + prices[i])

        # return dfs(n-1,False)