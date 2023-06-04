import pandas as pd
df= pd.read_csv("fake_or_real_news.csv")
# print(df.head())

"""

TfidfVectorizer for text classification
Similar to the sparse CountVectorizer created in the previous exercise, you'll work on creating tf-idf vectors for your documents. You'll set up a TfidfVectorizer and investigate some of its features.

In this exercise, you'll use pandas and sklearn along with the same X_train, y_train and X_test, y_test DataFrames and Series you created in the last exercise.

Instructions
100 XP
Import TfidfVectorizer from sklearn.feature_extraction.text.
Create a TfidfVectorizer object called tfidf_vectorizer. When doing so, specify the keyword arguments stop_words="english" and max_df=0.7.
Fit and transform the training data.
Transform the test data.
Print the first 10 features of tfidf_vectorizer.
Print the first 5 vectors of the tfidf training data using slicing on the .A (or array) attribute of tfidf_train.
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

# Print the first 10 features
print(tfidf_vectorizer.get_feature_names_out()[:10])

# Print the first 5 vectors of the tfidf training data
print(tfidf_train.A[:5])
"""tfidf_train.A converts the sparse matrix representation to a dense array for better readability."""

"""
sparse not clear
  (0, 0)    0.2
  (1, 2)    0.4
  (2, 1)    0.3
  
  dense array more clear
[[0.2 0.  0. ]
 [0.  0.  0.4]
 [0.  0.3 0. ]]

"""