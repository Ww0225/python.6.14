# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 你可以按 任何顺序 返回答案。
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(i):
            d = k - len(path)
            if i < d:
                return

            if len(path) == k:
                ans.append(path.copy())

            for j in range(i,0,-1):
                path.append(j)
                dfs(j-1)
                path.pop()

        dfs(n)
        return ans