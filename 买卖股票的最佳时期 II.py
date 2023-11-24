# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。
from math import inf

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        f0 = 0
        f1 = -inf
        for p in prices:
            new_f0 = max(f0,f1 + p)
            f1 = max(f1,f0 - p)
            f0 = new_f0
            # f[i+1][0] = max(f[i][0],f[i][1] + p)
            # f[i+1][1] = max(f[i][1],f[i][0] - p)
        return f0

        # @cache
        # def dfs(i,hold):
        #     if i < 0:
        #         return -inf if hold else 0
        #     if hold:
        #         return max(dfs(i-1,True),dfs(i-1,False) - prices[i])
        #     return max(dfs(i-1,False),dfs(i-1,True) + prices[i])

        # return dfs(n-1,False)