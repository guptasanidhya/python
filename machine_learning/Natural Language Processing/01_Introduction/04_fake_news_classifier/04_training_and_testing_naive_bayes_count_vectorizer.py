import pandas as pd
df= pd.read_csv("fake_or_real_news.csv")
# print(df.head())

"""
Now it's your turn to train the "fake news" model using the features you identified and extracted. In this first exercise you'll train and test a Naive Bayes model using the CountVectorizer data.

The training and test sets have been created, and count_vectorizer, count_train, and count_test have been computed.

Instructions
70 XP
Import the metrics module from sklearn and MultinomialNB from sklearn.naive_bayes.
Instantiate a MultinomialNB classifier called nb_classifier.
Fit the classifier to the training data.
Compute the predicted tags for the test data.
Calculate and print the accuracy score of the classifier.
Compute the confusion matrix. To make it easier to read, specify the keyword argument labels=['FAKE', 'REAL'].
"""
# Import the necessary modules
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split


# Create a series to store the labels: y
y = df.label
# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df["text"],y,test_size=0.33,random_state=53)

# Initialize a CountVectorizer object: count_vectorizer
count_vectorizer = CountVectorizer(stop_words="english")
# Transform the training data using only the 'text' column values: count_train
count_train = count_vectorizer.fit_transform(X_train)

# Transform the test data using only the 'text' column values: count_test
count_test = count_vectorizer.transform(X_test)

# Import the necessary modules
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB

# Instantiate a Multinomial Naive Bayes classifier: nb_classifier
nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(count_train,y_train)

# Create the predicted tags: pred
pred = nb_classifier.predict(count_test)

# Calculate the accuracy score: score
score = metrics.accuracy_score(y_test,pred)
print(score)

# Calculate the confusion matrix: cm
cm = metrics.confusion_matrix(y_test,pred,labels=['FAKE','REAL'])
print(cm)
