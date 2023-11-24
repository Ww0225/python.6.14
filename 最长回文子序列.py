# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]

        # @cache
        # def dfs(i,j):
        #     if i > j:
        #         return 0
        #     if i == j:
        #         return 1
        #     if s[i] == s[j]:
        #         return dfs(i+1,j-1) + 2
        #     return max(dfs(i+1,j),dfs(i,j-1))

        # return dfs(0,n-1)