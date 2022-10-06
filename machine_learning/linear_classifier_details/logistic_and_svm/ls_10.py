from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
df=datasets.load_digits()
x=df.data
y=df.target
lr = LogisticRegression()
lr.fit(x,y)

# Get predicted probabilities
proba = lr.predict_proba(x)

# Sort the example indices by their maximum probability
proba_inds = np.argsort(np.max(proba,axis=1))
print(proba_inds)
# Show the most confident (least ambiguous) digit
most=proba_inds[-1]

# Show the least confident (most ambiguous) digit
least=proba_inds[0]
plt.imshow(df.images[most], cmap=plt.cm.gray_r, interpolation='nearest')
# plt.imshow(df.images[least], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

"""
Visualizing easy and difficult examples
In this exercise, you'll visualize the examples that the logistic regression model is most and least confident about by looking at the largest and smallest predicted probabilities.

The handwritten digits dataset is already loaded into the variables X and y. The show_digit function takes in an integer index and plots the corresponding image, with some extra information displayed above the image.
Fill in the first blank with the index of the digit that the model is most confident about.
Fill in the second blank with the index of the digit that the model is least confident about.
Observe the images: do you agree that the first one is less ambiguous than the second?

Hint
proba_inds contains the information you need. The first element of proba_inds corresponds to the index of the digit that the model is most least confident about. The second element corresponds to the index of the digit that the model is next least confident about. Etc.
"""