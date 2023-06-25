"""
Step 2: Building a vectorizer
In this exercise, you are asked to build a TfIDf transformation of the review column in the reviews dataset. You are asked to specify the n-grams, stop words, the pattern of tokens and the size of the vocabulary arguments.

This is the last step before we train a classifier to predict the sentiment of a review.

Make sure you specify the maximum number of features properly, as a very large vocabulary size could disconnect your session.

Instructions
100 XP
Import the Tfidf vectorizer and the default list of English stop words.
Build the Tfidf vectorizer, specifying - in this order - the following arguments: use as stop words the default list of English stop words; as n-grams use uni- and bi-grams;the maximum number of features should be 200; capture only words using the specified pattern.
Create a DataFrame using the Tfidf vectorizer."""


from nltk.tokenize import word_tokenize
import pandas as pd

reviews=pd.read_csv("amazon_reviews_sample.csv")

# Tokenize each item in the review column
word_tokens = [word_tokenize(review) for review in reviews.review]

# Create an empty list to store the length of the reviews
len_tokens = []

# Iterate over the word_tokens list and determine the length of each item
for i in range(len(word_tokens)):
     len_tokens.append(len(word_tokens[i]))

# Create a new feature for the lengh of each review
reviews['n_words'] = len_tokens
print("######################################################## original task")
# Import the TfidfVectorizer and default list of English stop words
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS,TfidfVectorizer

# Build the vectorizer
vect = TfidfVectorizer(stop_words=ENGLISH_STOP_WORDS, ngram_range=(1, 2), max_features=200, token_pattern=r'\b[^\d\W][^\d\W]+\b').fit(reviews.review)
# Create sparse matrix from the vectorizer
X = vect.transform(reviews.review)

# Create a DataFrame
reviews_transformed = pd.DataFrame(X.toarray(), columns=vect.get_feature_names())
print('Top 5 rows of the DataFrame: \n', reviews_transformed.head())