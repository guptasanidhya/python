"""Specify the token pattern
In this exercise, you will work with the text column of the tweets dataset. Your task is to vectorize the object column using CountVectorizer. You will apply different patterns of tokens in the vectorizer. Remember that by specifying the token pattern, you can filter out characters.

The CountVectorizer has been imported for you.

Instructions 1/2
50 XP
Build a vectorizer from the text column, specifying the pattern of tokens to be equal to r'\b[^\d\W][^\d\W]'

Instructions 2/2
0 XP
Build a vectorizer from the text column using the default values of the function's arguments.
Build a second vectorizer, specifying the pattern of tokens to be equal to r'\b[^\d\W][^\d\W]'.


"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
tweets=pd.read_csv("Tweets.csv")

# # Build and fit the vectorizer
# vect = CountVectorizer(token_pattern=r'\b[^\d\W][^\d\W]+\b').fit(tweets.text)
# vect.transform(tweets.text)
# print('Length of vectorizer: ', len(vect.get_feature_names_out()))

# Build the first vectorizer
vect1 = CountVectorizer().fit(tweets.text)
vect1.transform(tweets.text)

# Build the second vectorizer
vect2 = CountVectorizer(token_pattern=r'\b[^\d\W][^\d\W]').fit(tweets.text)
vect2.transform(tweets.text)

# Print out the length of each vectorizer
print('Length of vectorizer 1: ', len(vect1.get_feature_names()))
print('Length of vectorizer 2: ', len(vect2.get_feature_names()))