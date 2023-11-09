a = 2
b = 1
sum_Fab = 0
for _ in range(100):
    sum_Fab += a/b
    a,b = a+b,a
print(f"数列的前100项和为：{sum_Fab}")
