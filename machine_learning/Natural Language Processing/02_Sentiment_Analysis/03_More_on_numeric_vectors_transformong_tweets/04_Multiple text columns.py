"""Multiple text columns
In this exercise, you will continue working with the airline Twitter data. A dataset tweets has been imported for you.

In some situations, you might have more than one text column in a dataset and you might want to create a numeric representation for each of the text columns. Here, besides the text column, which contains the body of the tweet, there is a second text column, called negativereason. It contains the reason the customer left a negative review.

Your task is to build BOW representations for both columns and specify the required stop words.

Instructions
100 XP
Import the vectorizer package and the default list of English stop words.
Update the default list of English stop words and create the my_stop_words set.
Specify the stop words argument in the first vectorizer to the updated set, and in the second vectorizer - the default set of English stop words."""
# Import the vectorizer and default English stop words list
from sklearn.feature_extraction.text import CountVectorizer, ENGLISH_STOP_WORDS
import pandas as pd
tweets=pd.read_csv("Tweets.csv")
# print(tweets)
# Define the stop words
my_stop_words = ENGLISH_STOP_WORDS.union(['airline', 'airlines', '@', 'am', 'pm'])

# Build and fit the vectorizers
vect1 = CountVectorizer(stop_words=my_stop_words)
vect2 = CountVectorizer(stop_words=ENGLISH_STOP_WORDS)

# Preprocess the 'negativereason' column by filling missing values
tweets['negativereason'].fillna('', inplace=True)

vect1.fit(tweets.text)
vect2.fit(tweets.negativereason)

# Print the last 15 features from the first, and all from second vectorizer
print(vect1.get_feature_names()[-15:])
print(vect2.get_feature_names())