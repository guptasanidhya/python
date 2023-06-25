"""Logistic regression of movie reviews
In the video we learned that logistic regression is a common way to model a classification task, such as classifying the sentiment as positive or negative.

In this exercise, you will work with the movies reviews dataset. The label column stores the sentiment, which is 1 when the review is positive, and 0 when negative. The text review has been transformed, using BOW, to numeric columns.

Your task is to build a logistic regression model using the movies dataset and calculate its accuracy.

Instructions
0 XP
Import the logistic regression function.
Create and fit a logistic regression on the labels y and the features X.
Calculate the accuracy of the logistic regression model, using the default .score() method.

"""
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
# Load the dataset
movies = pd.read_csv("IMDB_sample.csv")

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

# Calculate the accuracy of the logistic regression model on the testing data
accuracy = log_reg.score(X_test, y_test)
print('Accuracy of logistic regression: ', accuracy)
