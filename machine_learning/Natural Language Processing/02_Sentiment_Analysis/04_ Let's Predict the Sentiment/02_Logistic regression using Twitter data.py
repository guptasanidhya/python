"""Logistic regression using Twitter data
In this exercise, you will build a logistic regression model using the tweets dataset. The target is given by the airline_sentiment, which is 0 for negative tweets, 1 for neutral, and 2 for positive ones. So, in this case, you are given a multi-class classification task. Everything we learned about binary problems applies to multi-class classification problems as well.

You will evaluate the accuracy of the model using the two different approaches from the slides.

The logistic regression function and accuracy score have been imported for you.

Instructions
100 XP
Instructions
100 XP
Build and fit a logistic regression model using the defined X and y as arguments.
Calculate the accuracy of the logistic regression model.
Predict the labels.
Calculate the accuracy score using the predicted and true labels."""
# Define the vector of targets and matrix of features
import pandas as pd
from sklearn.metrics import accuracy_score

tweets=pd.read_csv("Tweets.csv")
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# Load the dataset
tweets = pd.read_csv("Tweets.csv")

# Split the dataset into features (X) and labels (y)
X = tweets['text']
y = tweets['airline_sentiment']

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

# Predict the labels using the trained model
y_pred = log_reg.predict(X_test)

# Calculate the accuracy score using the predicted and true labels
accuracy_score = accuracy_score(y_test, y_pred)
print('Accuracy score: ', accuracy_score)
