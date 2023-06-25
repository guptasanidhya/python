"""
BOW with n-grams and vocabulary size
In this exercise, you will practice building a bag-of-words once more, using the reviews dataset of Amazon product reviews. Your main task will be to limit the size of the vocabulary and specify the length of the token sequence.

Instructions
100 XP
Import the vectorizer from sklearn.
Build the vectorizer and make sure to specify the following parameters: the size of the vocabulary should be limited to 1000, include only bigrams, and ignore terms that appear in more than 500 documents.
Fit the vectorizer to the review column.
Create a DataFrame from the BOW representation.

"""
#Import the vectorizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
reviews=pd.read_csv("IMDB_sample.csv")

# Build the vectorizer, specify max features and fit
vect = CountVectorizer(max_features=1000, ngram_range=(2, 2), max_df=500)
vect.fit(reviews.review)

# Transform the review
X_review = vect.transform(reviews.review)

# Create a DataFrame from the bow representation
X_df = pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
print(X_df.head())