"""Tfidf and a BOW on same data
In this exercise, you will transform the review column of the Amazon product reviews using both a bag-of-words and a tfidf transformation.

Build both vectorizers, specifying only the maximum number of features to be equal to 100. Create DataFrames after the transformation and print the top 5 rows of each.

Be careful how you specify the maximum number of features in the vocabulary. A large vocabulary size can result in your session being disconnected.

Instructions
100 XP
Import the BOW and Tfidf vectorizers.
Build and fit a BOW and a Tfidf vectorizer from the review column and limit the number of created features to 100.
Create DataFrames from the transformed vector representations."""

# Import the required packages
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
import pandas as pd
reviews=pd.read_csv("IMDB_sample.csv")

# Build a BOW and tfidf vectorizers from the review column and with max of 100 features
vect1 = CountVectorizer(max_features=100).fit(reviews.review)
vect2 = TfidfVectorizer(max_features=100).fit(reviews.review)

# Transform the vectorizers
X1 = vect1.transform(reviews.review)
X2 = vect2.transform(reviews.review)
# Create DataFrames from the vectorizers
X_df1 = pd.DataFrame(X1.toarray(), columns=vect1.get_feature_names())
X_df2 = pd.DataFrame(X2.toarray(), columns=vect2.get_feature_names())
print('Top 5 rows using BOW: \n', X_df1.head())
print('Top 5 rows using tfidf: \n', X_df2.head())