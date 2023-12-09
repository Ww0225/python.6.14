# 题目描述
# 小蓝有一张黑白图像，由n×m个像素组成，其中从上到下共n
# 行，每行从左到右m列。每个像素由一个0到255之间的灰度值表
# 示。
# 现在，小蓝准备对图像进行模糊操作，操作的方法为：
# 对于每个像素，将以它为中心3×3区域内的所有像素（可能是9个
# 像素或少于9个像素)求和后除以这个范围内的像素个数（取下
# 整)，得到的值就是模糊后的结果。
# 请注意每个像素都要用原图中的灰度值计算求和。
# 输入描述
# 输入的第一行包含两个整数n,m。
# 第2行到第n十1行每行包含m个整数，表示每个像素的灰度值，
# 相邻整数之间用一个空格分隔。
# 其中，1≤n,m≤100。
# 输出描述
# 输出行，每行m个整数，相邻整数之间用空格分隔，表示模糊后
# 的图像。
n,m = map(int,input().split())
black = [list(map(int,input().split())) for _ in range(n)]
res = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        sum = 0
        count = 0
        for p in range(i-1,i+2):
            for q in range(j-1,j+2):
                if 0 <= q < m and 0 <= p < n:
                    sum += black[p][q]
                    count += 1
        res[i][j] = sum // count
for i in range(n):
    for j in range(m):
        print(res[i][j],end=' ')
    print()