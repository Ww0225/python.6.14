# 给你一个输入字符串 (s) 和一个字符模式 (p) ，请你实现一个支持 '?' 和 '*' 匹配规则的通配符匹配：
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符序列（包括空字符序列）。
# 判定匹配成功的充要条件是：字符模式必须能够 完全匹配 输入字符串（而不是部分匹配）。
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        zong = len(p)+1
        heng = len(s)+1
        table = [[False]*heng for _ in range(zong)]
        table[0][0]=True
        if p.startswith('*'):
            table[1] = [True]*heng
        for k in range(zong - 1):
            if p[k] == '*':
                table[k + 1][0] = True
            else:
                break
        for i in range(1,zong):
            path = False
            for j in range(1,heng):
                if p[i-1] == '*':
                    if table[i-1][0] == True:
                        table[i] = [True]*heng
                    if table[i-1][j] == True:
                        path = True
                    if path == True:
                        table[i][j] = True
                elif p[i-1] == '?' or p[i-1] == s[j-1]:
                    table[i][j] = table[i-1][j-1]
        return table[zong-1][heng-1]