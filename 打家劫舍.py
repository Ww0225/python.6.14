# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
# 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        cache = [-1]*n

        def dfs(i):
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            res = max(dfs(i-1),dfs(i-2)+nums[i])
            cache[i] = res
            return res

        return dfs(n-1)

        #法二:
        # n = len(nums)
        # f = [0]*(n+2)
        # for i,x in enumerate(nums):
        #     f[i+2]=max(f[i+1],f[i]+x)
        # return f[n+1]