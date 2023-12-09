# 删除字符
# 题目描述
# 给定一个单词，请问在单词中删除t个字母后，能得到的字典序最小
# 的单词是什么？
# 输入描述
# 输入的第一行包含一个单词，由大写英文字母组成。
# 第二行包含一个正整数t。
# 其中，单词长度不超过100，t小于单词长度。
# 输出描述
# 输出一个单问，表示答案。
s = input()
t = int(input())
for i in range(t):
    for j in range(len(s)-1):
        if s[j] > s[j+1]:
            s = s[:j] + s[j+1:]
            break
    else:
        s = s[0:len(s)-1]
print(s)