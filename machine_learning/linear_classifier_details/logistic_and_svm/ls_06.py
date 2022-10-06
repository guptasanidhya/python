from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
df=datasets.load_digits()

x=df.data
y=df.target
x_train,x_valid,y_train,y_valid=train_test_split(x,y,test_size=0.2,random_state=42)
# Train and validaton errors initialized as empty list
train_errs = list()
valid_errs = list()

# Loop over values of C_value
C_values=[0.001, 0.01, 0.1, 1, 10, 100, 1000]
for C_value in C_values:
    # Create LogisticRegression object and fit
    lr = LogisticRegression(C=C_value)
    lr.fit(x_train, y_train)

    # Evaluate error rates and append to lists
    train_errs.append(1.0 - lr.score(x_train, y_train))
    valid_errs.append(1.0 - lr.score(x_valid, y_valid))

# Plot results
plt.semilogx(C_values, train_errs, C_values, valid_errs)
plt.legend(("train", "validation"))
plt.show()
"""
The handwritten digits dataset is already loaded, split, and stored in the variables X_train, y_train, X_valid, and y_valid. The variables train_errs and valid_errs are already initialized as empty lists.

Instructions
0 XP
Loop over the different values of C_value, creating and fitting a LogisticRegression model each time.
Save the error on the training set and the validation set for each model.
Create a plot of the training and testing error as a function of the regularization parameter, C.
Looking at the plot, what's the best value of C?
"""