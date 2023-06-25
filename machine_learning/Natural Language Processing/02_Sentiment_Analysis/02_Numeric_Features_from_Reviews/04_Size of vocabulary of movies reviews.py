"""
Size of vocabulary of movies reviews
In this exercise, you will practice different ways to limit the size of the vocabulary using a sample of the movies reviews dataset. The first column is the review, which is of type object and the second column is the label, which is 0 for a negative review and 1 for a positive one.

The three methods that you will use will transform the text column to new numeric columns, capturing the count of a word or a phrase in each review. Each method will ultimately result in building a different number of new features.

Instructions 3/3
30 XP
Using the movies dataset, limit the size of the vocabulary to 100.

Using the movies dataset, limit the size of the vocabulary to include terms which occur in no more than 200 documents.

Using the movies dataset, limit the size of the vocabulary to ignore terms which occur in less than 50 documents.

"""

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
movies=pd.read_csv("IMDB_sample.csv")

# Build the vectorizer, specify size of vocabulary and fit
vect = CountVectorizer(max_features=100,max_df=200,min_df=50)
vect.fit(movies.review)

# Transform the review column
X_review = vect.transform(movies.review)
# Create the bow representation
X_df = pd.DataFrame(X_review.toarray(), columns=vect.get_feature_names())
print(X_df.head())