# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
# 元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次
class Solution:
    def reverseVowels(self, s: str) -> str:
        check_list = ['a','o','e','u','i','A','O','E','I','U']
        left,right = 0,len(s)-1
        s_list = list(s)
        while left < right:
            if s_list[left] in check_list and s_list[right] in check_list:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left+=1
                right-=1
            if s_list[left] not in check_list:
                left +=1
            if s_list[right] not in check_list:
                right-=1
        return ''.join(s_list)