"""Build and assess a model: movies reviews
In this problem, you will build a logistic regression model using the movies dataset. The score is stored in the label column and is 1 when the review is positive, and 0 when negative. The text review has been transformed, using BOW, to numeric columns.

You have already built a classifier but evaluated it using the same data employed in the training step. Make sure you now assess the model using an unseen test dataset. How does the performance of the model change when evaluated on the test set?

Instructions
100 XP
Import the function required for a train/test split.
Perform the train/test split, specifying that 20% of the data should be used as a test set.
Train a logistic regression model.
Print out the accuracy of the model on the training and on the testing data.

"""
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

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a logistic regression model and fit it to the training data
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

# Build a logistic regression model and print out the accuracy
log_reg = LogisticRegression().fit(X_train,y_train)
print('Accuracy on train set: ', log_reg.score(X_train, y_train))
print('Accuracy on test set: ', log_reg.score(X_test, y_test))