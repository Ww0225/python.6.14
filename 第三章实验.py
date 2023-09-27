# 5、敏感词过滤。敏感词是指带有敏感政治倾向、暴力倾向、不健康色彩的词或不文明的词语。
# 请使用字符串中的replace、sub等方法模拟敏感词过滤，将含有敏感词的字语句使用对应长度的“*”符号替换。
# words = "不好，傻，丑".split("，")
# content = input("请输入你的语句：")
# for i in words:
#     if i in content:
#         content = content.replace(i,len(i)*'*')
# print(content)
#3、编程程序：匹配合法的身份证号码（15或18位）。
# 从键盘上输入一串字符（身份证号），然后进行匹配，根据匹配结果输出是否是合法的身份证号。
# import re
# id = input("请输入你的身份证号(15或18位):")
# str1 = "\d{17}[0-9a-zA-Z]|\d{14}[0-9a-zA-Z]"
# pattern = re.compile(str1)
# print(re.match(pattern,id))
#6、附加题：统计每个英文单词的个数（频次）。
# 思路如下：
# (1)、从键盘上输入一段英文字符串，并将该字符串赋值给某个变量。
# (2)、使用正则表达式，以非英文字符为间隔符，切片（调用split函数完成），此操作会生成一个以单词为基本元素的list列表。
# (3)、由于原先非字母可能连续，故生成的list可能存在空单词，需要去除空字符串。
# (4)、全部转成小写，并排序。
# (5)、将单词顺次存入dict，如果单词存在，则个数加一，如果不存在，则将此单词存入dict，个数设置为1。
# (6)、输出。
import re
str = input("请输入一段英文字符串:")
str1 = "[^0-9a-zA-Z]"
pattern = re.compile(str1)
list = re.split(pattern,str)
list = [x.strip().lower() for x in list if x != '']
list = sorted(list)
dict = {}
for i in list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
print(dict)