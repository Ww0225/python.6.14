from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
filename = "moumou.csv"
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(filename,names=names)
array = data.values
X = array[:,0:8]
y = array[:,8]

transformer = MinMaxScaler(feature_range=(0,1))
newX = transformer.fit_transform(X)
set_printoptions(precision=3)
print(newX)
#正态化
transformer = StandardScaler().fit_transform(X)
newX = transformer.transform(X)
set_printoptions(precision=3)
print(newX)
#标准化处理
transformer = Binarizer(threshold=0.0).fit(X)
newX = transformer.transform(X)
set_printoptions(precision=3)
print(newX)
