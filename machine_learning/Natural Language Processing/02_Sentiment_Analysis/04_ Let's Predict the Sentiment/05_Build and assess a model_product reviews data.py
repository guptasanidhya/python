"""Build and assess a model: product reviews data
In this exercise, you will build a logistic regression using the reviews dataset, containing customers' reviews of Amazon products. The array y contains the sentiment : 1 if positive and 0 otherwise. The array X contains all numeric features created using a BOW approach. Feel free to explore them in the IPython Shell.

Your task is to build a logistic regression model and calculate the accuracy and confusion matrix using the test dataset.

The logistic regression and train/test splitting functions have been imported for you.

Instructions
100 XP
Import the accuracy score and confusion matrix functions.
Split the data into training and testing, using 30% of it as a test set and set the random seed to 42.
Train a logistic regression model.
Print out the accuracy score and confusion matrix using the test data."""
# Import the accuracy and confusion matrix
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
# Load the dataset
reviews = pd.read_csv("amazon_reviews_sample.csv")
# Split the dataset into features (X) and labels (y)
X = reviews['review']
y = reviews['score']

# Convert the text reviews into numerical features using BOW
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)


# Split the data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=42)

# Build a logistic regression
log_reg = LogisticRegression().fit(X_train,y_train)

# Predict the labels
y_predict = log_reg.predict(X_test)

# Print the performance metrics
print('Accuracy score of test data: ', accuracy_score(y_test,y_predict))
print('Confusion matrix of test data: \n', confusion_matrix(y_test, y_predict)/len(y_test))