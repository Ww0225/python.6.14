from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

filename = "moumou.csv"
names = ['mou','moumou']
data = read_csv(filename,names=names)
array = data.values
X = array[:,0:8]
Y = array[:,8]
num_folds = 10
seed = 7
kfold = KFold(n_splits=num_folds,random_state=seed,shuffle=True)

#基模型
cart = DecisionTreeClassifier()
num_tree = 100
model = BaggingClassifier(base_estimater=cart,n_estimators=num_tree,random_state=seed)
result = cross_val_score(model,X,Y,cy=kfold)
print(result.mean())

#随机森林
from sklearn.ensemble import RandomForestClassifier
num_tree = 100
max_features = 3
model = RandomForestClassifier(n_estimators=num_tree,random_state=seed,max_features=max_features)
result = cross_val_score(model,X,Y,cy=kfold)
print(result.mean())

#极端随机数
from sklearn.ensemble import ExtraTreesClassifier
max_features = 7
model = ExtraTreesClassifier(n_estimators=num_tree,max_features=max_features,random_state=seed)
result = cross_val_score(model,X,Y,cy=kfold)
print(result.mean())

#Adaboost
from sklearn.ensemble import AdaBoostClassifier
num_tree = 30
model = AdaBoostClassifier(n_estimators=num_tree,max_features=max_features,random_state=seed)
result = cross_val_score(model,X,Y,cy=kfold)
print(result.mean())

#随机梯度提升
from sklearn.ensemble import GradientBoostingClassifier
num_tree = 100
model = GradientBoostingClassifier(n_estimators=num_tree,random_state=seed)
result = cross_val_score(model,X,Y,cy=kfold)
print(result.mean())

#投票算法
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
models = []
model_logistic = LogisticRegression()
models.append(('logistic',model_logistic))
model_cart = DecisionTreeClassifier()
models.append(('cart',model_cart))
model_svc = SVC()
models.append(('svm',model_svc))
ensemble_model = VotingClassifier(estimators=models)
result = cross_val_score(ensemble_model,X,Y,cy=kfold)
print(result.mean())
