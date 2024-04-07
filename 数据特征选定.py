from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
filename = "moumou.csv"
names = ['mou','moumou']
data = read_csv(filename,names=names)
array = data.values
X = array[:,0:8]
Y = array[:,8]
test = SelectKBest(score_func=chi2,k=4)
fit = test.fit(X,Y)
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
print(features)

#RFE
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
rfe = RFE(model,n_features_to_select=3)
fit = rfe.fit(X,Y)
print('特征个数：')
print(fit.n_features_)
print('被选定特征：')
print(fit.support_)
print('特征排名：')
print(fit.ranking)

#PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
fit = pca.fit(X)
print('解释方差：%s' %fit.explained_variance_ratio_)
print(fit.components_)

#Extra Trees classifier
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
fit = model.fit(X,Y)
print(fit.feature_importances_)