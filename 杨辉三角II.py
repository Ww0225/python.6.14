# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = []
        for i in range(rowIndex+1):
            row = []
            for j in range(0,i+1):
                if j==0 or j==i:
                    row.append(1)
                else:
                    row.append(res[i-1][j]+res[i-1][j-1])
            res.append(row)
        return res[rowIndex]