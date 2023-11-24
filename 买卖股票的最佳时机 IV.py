# 给你一个整数数组 prices 和一个整数 k ，其中 prices[i] 是某支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
from math import inf


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        f = [[[-inf]*2 for _ in range(k+2)] for _ in range(n+1)]
        for j in range(1,k+2):
            f[0][j][0] = 0
        for i,p in enumerate(prices):
            for j in range(1,k+2):
                f[i+1][j][0] = max(f[i][j][0],f[i][j-1][1] + p)
                f[i+1][j][1] = max(f[i][j][1],f[i][j][0] - p)
        return f[n][k+1][0]
        # @cache
        # def dfs(i,j,hold):
        #     if j < 0:
        #         return -inf
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i-1,j,True),dfs(i-1,j,False) - prices[i])
        #     return max(dfs(i-1,j,False),dfs(i-1,j-1,True) + prices[i])

        # return dfs(n-1,k,False)