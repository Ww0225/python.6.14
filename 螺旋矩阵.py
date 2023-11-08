# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []
        left,right,top,base,res=0,len(matrix[0])-1,0,len(matrix)-1,[]
        while True:
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top += 1
            if top>base:
                break
            for i in range(top,base+1):
                res.append(matrix[i][right])
            right-=1
            if left>right:
                break
            for i in range(right,left-1,-1):
                res.append(matrix[base][i])
            base -= 1
            if top>base:
                break
            for i in range(base,top-1,-1):
                res.append(matrix[i][left])
            left+=1
            if left>right:
                break
        return res