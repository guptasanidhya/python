from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC

df=datasets.load_digits()

x=df.data
y=df.target
z=df.feature_names
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Instantiate the GridSearchCV object and run the search
# We set random_state=0 for reproducibility
linear_classifier = SGDClassifier(random_state=0)

# Instantiate the GridSearchCV object and run the search
parameters = {'alpha':[0.00001, 0.0001, 0.001, 0.01, 0.1, 1],
             'loss':['hinge', 'log_loss']}
searcher = GridSearchCV(linear_classifier, parameters, cv=10)
searcher.fit(x_train, y_train)

# Report the best parameters and the corresponding score
print("Best CV params", searcher.best_params_)
print("Best CV accuracy", searcher.best_score_)
print("Test accuracy of best grid search hypers:", searcher.score(x_test, y_test))

"""
Using SGDClassifier
In this final coding exercise, you'll do a hyperparameter search over the regularization strength and the loss (logistic regression vs. linear SVM) using SGDClassifier().

Instructions
0 XP
Instantiate an SGDClassifier instance with random_state=0.
Search over the regularization strength and the hinge vs. log_loss losses.
"""