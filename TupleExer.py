t1_stu = ("ww",21,['basketball','majiang'])
index = t1_stu.index(21)
print(index)
print(t1_stu[0])
del t1_stu[2][0]
print(t1_stu)
t1_stu[2].append("coding")
print(t1_stu)