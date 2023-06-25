import pandas as pd
import numpy as np
df= pd.read_csv("fake_or_real_news.csv")
# print(df.head())
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
# Initialize a TfidfVectorizer object: tfidf_vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
"""max_df=0.7 ignores terms that appear in more than 70% of the documents."""
# Create a series to store the labels: y
y = df.label
# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df["text"],y,test_size=0.33,random_state=53)


# Transform the training data: tfidf_train
tfidf_train = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data: tfidf_test
tfidf_test = tfidf_vectorizer.transform(X_test)

# Import the necessary modules
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB

"""______________________________________________________________________________________________________________"""
"""Your job in this exercise is to test a few different alpha levels using the Tfidf vectors to determine if there is a better performing combination.

The training and test sets have been created, and tfidf_vectorizer, tfidf_train, and tfidf_test have been computed.

Instructions
100 XP
Instructions
100 XP
Create a list of alphas to try using np.arange(). Values should range from 0 to 1 with steps of 0.1.
Create a function train_and_predict() that takes in one argument: alpha. The function should:
Instantiate a MultinomialNB classifier with alpha=alpha.
Fit it to the training data.
Compute predictions on the test data.
Compute and return the accuracy score.
Using a for loop, print the alpha, score and a newline in between. Use your train_and_predict() function to compute the score. Does the score change along with the alpha? What is the best alpha?


"""

# Create the list of alphas: alphas
alphas = np.arange(0,1,0.1)

# Define train_and_predict()
def train_and_predict(alpha):
    # Instantiate the classifier: nb_classifier
    nb_classifier = MultinomialNB(alpha=alpha)
    # Fit to the training data
    nb_classifier.fit(tfidf_train,y_train)
    # Predict the labels: pred
    pred = nb_classifier.predict(tfidf_test)
    # Compute accuracy: score
    score = metrics.accuracy_score(y_test,pred)
    return score

# Iterate over the alphas and print the corresponding score
for alpha in alphas:
    print('Alpha: ', alpha)
    print('Score: ', train_and_predict(alpha))
    print()
