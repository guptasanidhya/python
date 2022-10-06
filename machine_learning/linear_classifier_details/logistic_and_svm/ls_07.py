from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
df=datasets.load_wine()

x=df.data
y=df.target
z=df.feature_names
print(z)
x_train,x_valid,y_train,y_valid=train_test_split(x,y,test_size=0.2,random_state=42)
# Specify L1 regularization
lr = LogisticRegression(solver='liblinear',penalty='l1' )

# Instantiate the GridSearchCV object and run the search
searcher = GridSearchCV(lr, {'C':[0.001, 0.01, 0.1, 1, 10]})
searcher.fit(x_train, y_train)

# Report the best parameters
print("Best CV params", searcher.best_params_)

# Find the number of nonzero coefficients (selected features)
best_lr = searcher.best_estimator_
coefs = best_lr.coef_
# print(coefs)
print("Total number of features:", coefs.size)
print("Number of selected features:", np.count_nonzero(coefs))
