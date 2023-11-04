# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
# 示例1:
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"abc"，所以其长度为3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic,res,i={},0,-1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]],i)
            dic[s[j]] = j
            res = max(res,j-i)
        return res