"""String operators with the Twitter data
You continue working with the tweets data where the text column stores the content of each tweet.

Your task is to turn the text column into a list of tokens. Then, using string operators, remove all non-alphabetic characters from the created list of tokens.

Instructions
100 XP
Import the word tokenizing function.
Create word tokens from each tweet.
Filter out all non-alphabetic characters from the created list, i.e. retain only letters."""
# Import the word tokenizing package
from nltk import word_tokenize
import pandas as pd
tweets=pd.read_csv("Tweets.csv")

# Tokenize the text column
word_tokens = [word_tokenize(review) for review in tweets.text]
print('Original tokens: ', word_tokens[0])

# Filter out non-letter characters
cleaned_tokens = [[word for word in item if word.isalpha()] for item in word_tokens]
print('Cleaned tokens: ', cleaned_tokens[0])