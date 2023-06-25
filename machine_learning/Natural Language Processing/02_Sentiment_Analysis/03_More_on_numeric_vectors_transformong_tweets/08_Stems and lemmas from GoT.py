"""Stems and lemmas from GoT
In this exercise, you are given a couple of sentences from George R.R. Martin's Game of Thrones. Your task is to create stems and lemmas from the given GoT string.

Remember that stems reduce a word to its root whereas lemmas produce an actual word. However, speed can differ significantly between the methods with stemming being much faster. In Steps 2 and 3, pay attention to the total time it takes to perform each operation. We're making use of the time.time() method to measure the time it takes to perform stemming and lemmatization.

Instructions 1/3
35 XP
Import the stemming and lemmatization functions.
Build a list of tokens from the GoT string.

Instructions 2/3
35 XP
Using list comprehension and the porter stemmer you imported, create the stemmed_tokens list.

Instructions 3/3
30 XP
Using list comprehension and the WNlemmatizer you imported, create the lem_tokens list.
"""
# Import the required packages from nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk import word_tokenize
GoT='Never forget what you are, for surely the world will not. Make it your strength. Then it can never be your weakness. Armour yourself in it, and it will never be used to hurt you.'

porter = PorterStemmer()
WNlemmatizer = WordNetLemmatizer()

# Tokenize the GoT string
tokens = word_tokenize(GoT)
print("################################################")
import time

# Log the start time
start_time = time.time()

# Build a stemmed list
stemmed_tokens = [porter.stem(token) for token in tokens]

# Log the end time
end_time = time.time()

print('Time taken for stemming in seconds: ', end_time - start_time)
print('Stemmed tokens: ', stemmed_tokens)

print("#####################################################################")
import time

# Log the start time
start_time = time.time()

# Build a lemmatized list
lem_tokens = [WNlemmatizer.lemmatize(token) for token in tokens]

# Log the end time
end_time = time.time()

print('Time taken for lemmatizing in seconds: ', end_time - start_time)
print('Lemmatized tokens: ', lem_tokens)