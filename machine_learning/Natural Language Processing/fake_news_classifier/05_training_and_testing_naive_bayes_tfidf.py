import pandas as pd
df= pd.read_csv("fake_or_real_news.csv")
# print(df.head())

"""
Training and testing the "fake news" model with TfidfVectorizer
Now that you have evaluated the model using the CountVectorizer, you'll do the same using the TfidfVectorizer with a Naive Bayes model.

The training and test sets have been created, and tfidf_vectorizer, tfidf_train, and tfidf_test have been computed. Additionally, MultinomialNB and metrics have been imported from, respectively, sklearn.naive_bayes and sklearn.

Instructions
100 XP
Instantiate a MultinomialNB classifier called nb_classifier.
Fit the classifier to the training data.
Compute the predicted tags for the test data.
Calculate and print the accuracy score of the classifier.
Compute the confusion matrix. As in the previous exercise, specify the keyword argument labels=['FAKE', 'REAL'] so that the resulting confusion matrix is easier to read.
"""
# Import TfidfVectorizer
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


# Create a Multinomial Naive Bayes classifier: nb_classifier
nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(tfidf_train,y_train)

# Create the predicted tags: pred
pred = nb_classifier.predict(tfidf_test)

# Calculate the accuracy score: score
score = metrics.accuracy_score(y_test,pred)
print(score)

# Calculate the confusion matrix: cm
cm = metrics.confusion_matrix(y_test,pred,labels=['FAKE','REAL'])
print(cm)
