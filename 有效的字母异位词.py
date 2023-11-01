# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for ss in s:
            s_dict[ss] += 1
        for tt in t:
            t_dict[tt] += 1
        return s_dict == t_dict