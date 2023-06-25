"""Regularizing models with Twitter data
You will work with the Twitter data expressing customers' sentiment about airline companies. The X matrix of features and y vector of labels have been created for you. In addition, the training and testing split has been performed. You can work with the X_train, X_test, y_train and y_test arrays directly.

You will train regularized and a more flexible models and evaluate them using different model performance metrics.

All required packages have been imported for you.

Instructions
100 XP
Instructions
100 XP
Train two logistic regressions: one with regularization parameter of 100 and a second of 0.1.
Print the accuracy scores of both models.
Print the confusion matrix of each model."""

# Define the vector of targets and matrix of features
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix

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


# Split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=42)

# Build a logistic regression with regularizarion parameter of 100
log_reg1 = LogisticRegression(C=100).fit(X_train,y_train)
# Build a logistic regression with regularizarion parameter of 0.1
log_reg2 = LogisticRegression(C=0.1).fit(X_train,y_train)

# Predict the labels for each model
y_predict1 = log_reg1.predict(X_test)
y_predict2 = log_reg2.predict(X_test)

# Print performance metrics for each model
print('Accuracy of model 1: ', accuracy_score(y_test, y_predict1))
print('Accuracy of model 2: ', accuracy_score(y_test, y_predict2))
print('Confusion matrix of model 1: \n' , confusion_matrix(y_test, y_predict1)/len(y_test))
print('Confusion matrix of model 2: \n', confusion_matrix(y_test, y_predict2)/len(y_test))