# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
# 回文串 是正着读和反着读都一样的字符串。
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            for j in range(i,n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(i+1)
                    path.pop()

        dfs(0)
        return ans