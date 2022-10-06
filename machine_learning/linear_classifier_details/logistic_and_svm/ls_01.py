"""appling kNeighbors on news dataset """
from sklearn import datasets
newsgroups=datasets.fetch_20newsgroups_vectorized()
print(newsgroups.feature_names)
X, y = newsgroups.data, newsgroups.target
print(X.shape,y.shape)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
print(knn.score(X_train, y_train))
print(knn.score(X_test, y_test))
