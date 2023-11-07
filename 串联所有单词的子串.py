# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
#  s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。
# 例如，如果 words = ["ab","cd","ef"]，
# 那么 "abcdef"， "abefcd"，"cdabef"， "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。
# "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        import collections
        allwords = collections.Counter(words)
        wordNum = len(words)
        wordLen = len(words[0])
        res=[]
        for i in range(len(s)-wordNum*wordLen+1):
            subwords = collections.defaultdict(int)
            index = i
            while index < i + wordNum*wordLen:
                curword = s[index:index+wordLen]
                if curword not in allwords or subwords[curword] == allwords[curword]:
                    break
                subwords[curword]+=1
                index += wordLen
            if index == i+wordNum*wordLen:
                res.append(i)
        return res