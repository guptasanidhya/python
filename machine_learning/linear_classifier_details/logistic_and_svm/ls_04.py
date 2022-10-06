"""applying SVC on wine dataset"""
from sklearn import datasets
wine=datasets.load_wine()
from sklearn.svm import SVC
svm = SVC()
svm.fit(wine.data, wine.target);
print(svm.score(wine.data, wine.target))