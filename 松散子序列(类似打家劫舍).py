# 问题描述
# 给定一个仅含小写字母的字符串s,假设s的一个子序列t的第i个
# 字符对应了原字符串中的第P个字符。我们定义s的一个松散子序列
# 为：对于i>1总是有P一p-1≥2。设一个子序列的价值为其包
# 含的每个字符的价值之和(a~z分别为1~26)。
# 求s的松散子序列中的最大价值。
# 输入格式
# 输入一行包含一个字符串s。
# 输出格式
# 输出一行包含一个整数表示答案。
def dfs(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return max(0,ord(s[0])-96)
    dp = [0]*len(s)
    dp[1] = max(dp[0],ord(s[1])-96)
    for i in range(2,len(s)):
        dp[i] = max(dp[i-1],dp[i-2] + ord(s[i])-96)
    return dp[-1]

s = input()
print(dfs(s))