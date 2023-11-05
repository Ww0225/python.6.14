# 给你一个字符串 s，找到 s 中最长的回文子串。
# 如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            start = max(0,i-len(res)-1)
            tmp = s[start:i+1]
            if tmp == tmp[::-1]:
                res = tmp
            else:
                tmp = tmp[1:]
                if tmp == tmp[::-1]:
                    res = tmp
        return res