# 编写一个函数来查找字符串数组中的最长公共前缀
# 如果不存在公共前缀，返回空字符串""
# 示例1:
# 输入：strs = ["flower", "flow", "flight"]
# 输出："fl"
# 示例2：
# 输入：strs = ["dog", "racecar", "car"]

# 输出：""
# 解释：输入不存在公共前缀
strs = input().split()
str1 = min(strs)
str2 = max(strs)
longest_str = ""
for i in range(0,len(str1)):
    if str1[i] != str2[i]:
        longest_str = str1[:i]
    else:
        longest_str = str1
print(longest_str)
