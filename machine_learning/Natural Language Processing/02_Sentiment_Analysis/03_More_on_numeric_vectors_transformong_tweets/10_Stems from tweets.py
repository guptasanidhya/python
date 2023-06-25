"""Stems from tweets
In this exercise, you will work with an array called tweets. It contains the text of the airline sentiment data collected from Twitter.

Your task is to work with this array and transform it into a list of tokens using list comprehension. After that, iterate over the list of tokens and create a stem out of each token. Remember that list comprehensions are a one-line alternative to for loops.

Instructions
100 XP
Import the function we used to transform strings into stems.
Call the Porter stemmer function you just imported.
Using a list comprehension, create the list tokens. It should contain all the word tokens from the tweets array.
Iterate over the tokens list and apply the stemming function to each item in the list."""
# Import the function to perform stemming
from nltk.stem import PorterStemmer
from nltk import word_tokenize

# Call the stemmer
porter = PorterStemmer()
tweets=['@VirginAmerica What @dhepburn said.',
       "@VirginAmerica plus you've added commercials to the experience... tacky.",
       "@VirginAmerica I didn't today... Must mean I need to take another trip!",
        '@united he has no priority and Iove it',
       '@united Pleased to be a Premier Platinum',
       '@united how can you not put my bag on plane to Seattle. Flight 1212. Waiting  in line to talk to someone about my bag. Status should matter.']
# Transform the array of tweets to tokens
tokens = [word_tokenize(word) for word in tweets]
# Stem the list of tokens
stemmed_tokens = [[porter.stem(word) for word in tweet] for tweet in tokens]
# Print the first element of the list
print(stemmed_tokens[0])