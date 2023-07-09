"""BOW using product reviews
You practiced a BOW on a small dataset. Now you will apply it to a sample of Amazon product reviews. The data has been imported for you and is called reviews. It contains two columns. The first one is called score and it is 0 when the review is negative, and 1 when it is positive. The second column is called review and it contains the text of the review that a customer wrote. Feel free to explore the data in the IPython Shell.

Your task is to build a BOW vocabulary, using the review column.

Remember that we can call the .get_feature_names() method on the vectorizer to obtain a list of all the vocabulary elements.

Instructions
100 XP
Create a CountVectorizer object, specifying the maximum number of features.
Fit the vectorizer.
Transform the fitted vectorizer.
Create a DataFrame where you transform the sparse matrix to a dense array and make sure to correctly specify the names of columns"""
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
reviews=pd.read_csv("amazon_reviews_sample.csv")

# Build the vectorizer, specify max features
vect = CountVectorizer(max_features=100)
# Fit the vectorizer
vect.fit(reviews.review)

# Transform the review column
X_review = vect.transform(reviews.review)

# Create the bow representation
X_df=pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
print(X_df.head())