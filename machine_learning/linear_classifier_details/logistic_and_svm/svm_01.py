from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

df=datasets.load_digits()

x=df.data
y=df.target
z=df.feature_names

# Train a linear SVM
svm = SVC(kernel="linear")
svm.fit(x,y)
# plot_classifier(X, y, svm, lims=(11,15,0,6))

# Make a new data set keeping only the support vectors
print("Number of original examples", len(x))
print("Number of support vectors", len(svm.support_))
X_small = x[svm.support_]
y_small = y[svm.support_]
print(X_small,y_small)
# Train a new SVM using only the support vectors
svm_small = SVC(kernel="linear")
svm_small.fit(X_small, y_small)
# plot_classifier(X_small, y_small, svm_small, lims=(11,15,0,6))

"""
Effect of removing examples
Support vectors are defined as training examples that influence the decision boundary. In this exercise, you'll observe this behavior by removing non support vectors from the training set.

The wine quality dataset is already loaded into X and y (first two features only). (Note: we specify lims in plot_classifier() so that the two plots are forced to use the same axis limits and can be compared directly.)

Instructions
0 XP
Train a linear SVM on the whole data set.
Create a new data set containing only the support vectors.
Train a new linear SVM on the smaller data set.

Hint
svm.support_ returns the indices of the support vectors of the model svm. You can use this to directly index into X and y and return subsets containly only those examples. For example, X[svm.support_].
"""