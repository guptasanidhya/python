"""A feature for the length of a review
You have now worked with a string and a list with string items, it is time to use a larger sample of data.

Your task in this exercise is to create a new feature for the length of a review, using the familiar reviews dataset.

Instructions 1/2
50 XP
Import the word tokenizing function from the required package.
Apply the function to the review column of the reviews

Instructions 2/2
50 XP
Iterate over the created word_tokens list.
As you iterate, find the length of each item in the list and append it to the empty len_tokens list.
Create a new feature n_words in the reviews for the length of the reviews.
"""
# Import the needed packages
from nltk import word_tokenize
import pandas as pd

reviews=pd.read_csv("amazon_reviews_sample.csv")
# Tokenize each item in the review column
word_tokens = [word_tokenize(review) for review in reviews.review]

# Print out the first item of the word_tokens list
print(word_tokens[0])

print("#############################")
# Create an empty list to store the length of reviews
len_tokens = []

# Iterate over the word_tokens list and determine the length of each item
for i in range(len(word_tokens)):
     len_tokens.append(len(word_tokens[i]))

# Create a new feature for the lengh of each review
reviews['n_words'] = len_tokens