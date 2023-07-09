"""Product reviews with regularization
In this exercise, you will work once more with the reviews dataset of Amazon product reviews. A vector of labels y contains the sentiment : 1 if positive and 0 otherwise. The matrix X contains all numeric features created using a BOW approach.

You will need to train two logistic regression models with different levels of regularization and compare how they perform on the test data. Remember that regularization is a way to control the complexity of the model. The more regularized a model is, the less flexible it is but the better it can generalize. Models with higher level of regularization are often less accurate than non-regularized ones.

Instructions
100 XP
Split the data into a train and test sets.
Train a logistic regression with regularization parameter of 1000. Train a second logistic regression with regularization parameter equal to 0.001.
Print the accuracy scores of both models on the test set."""
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


# Split data into training and testing
X_train,X_test,y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Train a logistic regression with regularization of 1000
log_reg1 = LogisticRegression(C=1000).fit(X_train, y_train)
# Train a logistic regression with regularization of 0.001
log_reg2 =  LogisticRegression(C=0.001).fit(X_train, y_train)

# Print the accuracies
print('Accuracy of model 1: ', log_reg1.score(X_test,y_test))
print('Accuracy of model 2: ', log_reg2.score(X_test,y_test))