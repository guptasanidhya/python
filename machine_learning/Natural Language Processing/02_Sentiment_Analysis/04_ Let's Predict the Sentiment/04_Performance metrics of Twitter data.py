"""Performance metrics of Twitter data
You will train a logistic regression model that predicts the sentiment of tweets and evaluate its performance on the test set using different metrics.

A matrix X has been created for you. It contains features created with a BOW on the text column.

The labels are stored in a vector called y. Vector y is 0 for negative tweets, 1 for neutral, and 2 for positive ones.
Note that although we have 3 classes, it is still a classification problem. The accuracy still measures the proportion of correctly predicted instances. The confusion matrix will now be of size 3x3, each row will give the number of predicted cases for classes 2, 1, and 0, and each column - the true number of cases in class 2, 1, and 0.

All required packages have been imported for you.

Instructions
100 XP
Perform the train/test split, and stratify by y.
Train a a logistic regression classifier.
Predict the performance on the test set.
Print the accuracy score and confusion matrix obtained on the test set."""

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


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123, stratify=y)

# Train a logistic regression
log_reg = LogisticRegression().fit(X_train, y_train)

# Make predictions on the test set
y_predicted = log_reg.predict(X_test)

# Print the performance metrics
print('Accuracy score test set: ', accuracy_score(y_test, y_predicted))
print('Confusion matrix test set: \n', confusion_matrix(y_test, y_predicted)/len(y_test))