print("分别输入头和脚的值:")
head,foot = map(int,input().split())
flag = 0
for i in range(1,head):
    x = i
    y = head-i
    if 2*x + 4*y == foot:
        flag = 1
        print(f"鸡有{x}只，兔有{y}只")
print("" if flag==1 else "Data Error!")