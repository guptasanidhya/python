"""TfIdf on Twitter airline sentiment data
You will now build features using the TfIdf method. You will continue to work with the tweets dataset.

In this exercise, you will utilize what you have learned in previous lessons and remove stop words, use a token pattern and specify the n-grams.

The final output will be a DataFrame, of which the columns are created using the TfidfVectorizer(). Such a DataFrame can directly be passed to a supervised learning model, which is what we will tackle in the next chapter.

Instructions
100 XP
Import the required package to build a TfidfVectorizer and the ENGLISH_STOP_WORDS.
Build a TfIdf vectorizer from the text column of the tweets dataset, specifying uni- and bi-grams as a choice of n-grams, tokens which include only alphanumeric characters using the given token pattern, and the stop words corresponding to the ENGLISH_STOP_WORDS.
Transform the vectorizer, specifying the same column that you fit.
Specify the column names in the DataFrame() function."""
# Import the required vectorizer package and stop words list
from sklearn.feature_extraction.text import TfidfVectorizer,ENGLISH_STOP_WORDS
import pandas as pd

tweets=pd.read_csv("Tweets.csv")
# Define the vectorizer and specify the arguments
my_pattern = r'\b[^\d\W][^\d\W]+\b'
vect = TfidfVectorizer(ngram_range=(1, 2), max_features=100, token_pattern=my_pattern, stop_words=ENGLISH_STOP_WORDS).fit(tweets.text)

# Transform the vectorizer
X_txt = vect.transform(tweets.text)

# Transform to a data frame and specify the column names
X=pd.DataFrame(X_txt.toarray(), columns=vect.get_feature_names())
print('Top 5 rows of the DataFrame: ', X.head())