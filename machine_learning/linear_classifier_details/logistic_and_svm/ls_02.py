"""applying logistic on wine dataset"""
from sklearn import datasets
from sklearn.linear_model import  LogisticRegression

wine=datasets.load_wine()
lr=LogisticRegression()
lr.fit(wine.data,wine.target)
print(lr.score(wine.data,wine.target))
print(lr.predict_proba(wine.data[:1]))