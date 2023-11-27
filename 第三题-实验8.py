# 汉诺塔问题基于递归算法的实现。
# 据说古代有一座梵塔，塔内有3个底座A、B、C，A座上有64个盘子，
# 盘子大小不等，大的在下，小的在上。
# 有一个和尚想把这64个盘子从A座移到C座，但每次只能允许移动一个盘子，
# 在移动盘子的过程中可以利用B座，但任何时刻3个座上的盘子都必须始终保持大盘在下、小盘在上的顺序。
# 如果只有一个盘子，则不需要利用B座，直接将盘子从A移动到C即可。
# 和尚想知道这项任务的详细移动步骤和顺序。
def honoi(n,start,help,end):
    if n == 1:
        print(start,"->",end)
        return
    honoi(n-1,start,end,help)
    print(start,"->",end)
    honoi(n-1,help,start,end)

if __name__ == '__main__':
    n = int(input("请输入汉诺塔的层数："))
    honoi(n,"A","B","C")