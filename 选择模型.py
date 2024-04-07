from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
filename = "moumou.csv"
names = ['mou','moumou']
data = read_csv(filename,names=names)
array = data.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 4
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=test_size,random_state=seed)
model = LogisticRegression()
model.fit(X_train,Y_train)
result = model.score(X_test,Y_test)
print('算法评估结果：%.3f %%' %(result)*100)

#K折交叉验证
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
num_fold = 10
seed = 7
kfold = KFold(n_splits=num_fold,random_state=seed,suffle=True)
model = LogisticRegression(multi_class='multinomial',max_iter=3000)
result = cross_val_score(model,X,Y,cv=kfold)
print("算法结果：%.3f %% (%.3f%%)" %(result.mean()*100,result.std()*100))

#弃一交叉验证
from sklearn.model_selection import LeaveOneOut
loocv = LeaveOneOut()
model = LogisticRegression(multi_class='multinomial',max_iter=3000)
result = cross_val_score(model,X,Y,cv=loocv)
print("算法结果：%.3f %% (%.3f%%)" %(result.mean()*100,result.std()*100))

#重复随机分离
from sklearn.model_selection import ShuffleSplit
n_splits = 10
test_size = 0.33
seed = 7
kfold = ShuffleSplit(n_splits=n_splits,test_size=test_size,random_state=seed)
model = LogisticRegression(multi_class='multinomial',max_iter=3000)
result = cross_val_score(model,X,Y,cv=kfold)
print("算法结果：%.3f %% (%.3f%%)" %(result.mean()*100,result.std()*100))

#对数损失函数
num_flods = 10
seed = 7
kfold = KFold(n_splits=num_flods,random_state=seed)
model = LogisticRegression(multi_class='multinomial',max_iter=3000)
Scoring = 'neg_log_loss'
result = cross_val_score(model,X,Y,cv=kfold,scoring=Scoring)
print("Logloss：%.3f %% (%.3f%%)" %(result.mean()*100,result.std()*100))

#AUC图
num_flods = 10
seed = 7
kfold = KFold(n_splits=num_flods,random_state=seed)
model = LogisticRegression(multi_class='multinomial',max_iter=3000)
scoring = 'roc_auc'
result = cross_val_score(model,X,Y,cv=kfold,scoring=scoring)
print("AUC：%.3f %% (%.3f%%)" %(result.mean()*100,result.std()*100))

