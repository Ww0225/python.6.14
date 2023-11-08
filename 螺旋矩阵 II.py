# 给你一个正整数n ，生成一个包含1到n**2所有元素，且元素按顺时针顺序螺旋排列的nxn正方形矩阵matrix 。
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        left,right,top,base=0,n-1,0,n-1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        num,tar=1,n*n
        while num<=tar:
            for i in range(left,right+1):
                mat[top][i] = num
                num += 1
            top += 1
            for i in range(top,base+1):
                mat[i][right] = num
                num+=1
            right -= 1
            for i in range(right,left-1,-1):
                mat[base][i] = num
                num+=1
            base -= 1
            for i in range(base,top-1,-1):
                mat[i][left] = num
                num+=1
            left += 1
        return mat
