from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

df=datasets.load_digits()

x=df.data
y=df.target
z=df.feature_names
# Instantiate an RBF SVM
svm = SVC()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Instantiate the GridSearchCV object and run the search
parameters = {'C':[0.1, 1, 10, 100], 'gamma':[0.00001, 0.0001, 0.001, 0.01, 0.1]}
searcher = GridSearchCV(svm, parameters)
searcher.fit(x_train, y_train)

# Report the best parameters and the corresponding score
print("Best CV params", searcher.best_params_)
print("Best CV accuracy", searcher.best_score_)

# Report the test accuracy using these best parameters
print("Test accuracy of best grid search hypers:", searcher.score(x_test, y_test))