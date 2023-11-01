# 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
# 例如：
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
         return '' if columnNumber==0 \
             else self.convertToTitle((columnNumber-1)//26) + chr((columnNumber-1)%26+65)