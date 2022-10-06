"""applying linear svc on wine dataset"""
from sklearn import datasets
wine=datasets.load_wine()
from sklearn.svm import LinearSVC
svm = LinearSVC()
svm.fit(wine.data, wine.target)
print(svm.score(wine.data, wine.target))
