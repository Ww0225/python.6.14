import numpy as np
myarray = np.array([1,2,3])
print(myarray)
print(myarray.shape)

myarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(myarray)
print(myarray.shape)

print("第一行的数据： %s" %myarray[0])
print("最后一行的数据： %s" %myarray[-1])
print("整列的数据：%s" %myarray[:,2])
