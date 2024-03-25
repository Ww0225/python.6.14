import pandas as pd
import numpy as np
#series:一维数组:list
myarray = np.array([1,2,3])
index = ['a','b','c']
myseries = pd.Series(myarray,index=index)
print(myseries)
print("series的第一个元素：")
print(myseries[0])
print("series的c index的元素：")
print(myseries['c'])
#Dataframe:可以指定行和列的二维数组
myarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
rowindex = ['row1','row2','row3']
colname = ['col1','col2','col3']
mydataframe = pd.DataFrame(data=myarray,index=rowindex,columns=colname)
print("访问col3的数据")
print(mydataframe['col3'])
