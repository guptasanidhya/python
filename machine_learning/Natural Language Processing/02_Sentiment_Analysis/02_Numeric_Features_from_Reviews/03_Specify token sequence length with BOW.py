"""
Specify token sequence length with BOW
We saw in the video that by specifying different length of tokens - what we called n-grams - we can better capture the context, which can be very important.

In this exercise, you will work with a sample of the Amazon product reviews. Your task is to build a BOW vocabulary, using the review column and specify the sequence length of tokens.

Instructions
100 XP
Build the vectorizer, specifying the token sequence length to be uni- and bigrams.
Fit the vectorizer.
Transform the fitted vectorizer.
In the DataFrame, make sure to correctly specify the column names.
"""
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
reviews=pd.read_csv("amazon_reviews_sample.csv")

# Build the vectorizer, specify token sequence and fit
vect = CountVectorizer(ngram_range=(1,2),max_features=5000)
vect.fit(reviews.review)

# Transform the review column
X_review = vect.transform(reviews.review)

# Create the bow representation
X_df = pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
print(X_df.head())