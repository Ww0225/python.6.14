# 给定一个只包括'('，')'，'{'，'}'，'['，']'的字符串
# s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
# 示例1：
# 输入：s = "()"
# 输出：true
# 示例2：
# 输入：s = "()[]{}"
# 输出：true
# 示例3：
# 输入：s = "(]"
# 输出：false
kuohao_dict = {'(':')','{':'}','[':']','?':'?'}
s = input()
stack = ['?']
for i in s:
    if i in kuohao_dict:
        stack.append(i)
    elif i != kuohao_dict[stack.pop()]:
        print(False)
print(len(stack)==1)