# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
# 只使用数字1到9
# 每个数字 最多使用一次
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(i,t):
            d = k - len(path)
            if t < 0 or t > (i*2-d+1)*d//2:
                return
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i,0,-1):
                path.append(j)
                dfs(j-1,t-j)
                path.pop()

        dfs(9,n)
        return ans
