# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0,i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i-1][j]+ret[i-1][j-1])
            ret.append(row)
        return ret