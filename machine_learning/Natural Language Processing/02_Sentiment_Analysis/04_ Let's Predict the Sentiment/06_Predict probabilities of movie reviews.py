"""Predict probabilities of movie reviews
In this problem, you will build a logistic regression using the movies dataset. The labels are stored in the arrayy and the features in X.

Train the model on the training data. Instead of predicting classes, predict the probabilities that each instance in the test set belongs to each of the two classes.

The logistic regression and train/test splitting functions have been imported for you.

Instructions
100 XP
Instructions
100 XP
Split the data into training and testing set.
Train a logistic regression model.
Predict the probabilities for class 0 and for class 1 of the testing data. Class 0 is located as the first column in the predicted probabilities, and class 1 is the second one."""
# Import the required packages
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd

movies=pd.read_csv("IMDB_sample.csv")

# Split the dataset into features (X) and labels (y)
X = movies['review']
y = movies['label']

# Convert the text reviews into numerical features using BOW
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=321)

# Train a logistic regression
log_reg = LogisticRegression().fit(X_train,y_train)

# Predict the probability of the 0 class
prob_0 = log_reg.predict_proba(X_test)[:, 0]
# Predict the probability of the 1 class
prob_1 = log_reg.predict_proba(X_test)[:, 1]

print("First 10 predicted probabilities of class 0: ", prob_0[:10])
print("First 10 predicted probabilities of class 1: ", prob_1[:10])