# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串
# 字母和数字都属于字母数字字符
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false
class Solution:
    #法一
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for ss in s:
            if s.isalpha():
                s_list.append(ss.lower())
            elif s.isdigit():
                s_list.append(ss)
        return ''.join(s_list)[0::] == ''.join(s_list)[::-1]
    #法二
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list = [ss for ss in s if ss.isalnum()]
        return s_list == s_list[::-1]
    #法三
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left,right = 0,len(s)-1
        while left < right:
            if not s[left].isalnum():
                left+=1
            if not s[right].isalnum():
                right-=1
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
        return True