# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号
# 例如：
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ret = 0
        for s in columnTitle:
            ret = ret*26+ord(s)-64
        return ret