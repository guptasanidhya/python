"""Stem Spanish reviews
You will recall that in a previous chapter we used a language detection package to determine the language of different Amazon product reviews. In this exercise, you will first detect the languages in the non_english_reviews. The reviews are in multiple languages but you will select ONLY those in Spanish. Feel free to go back to the video discussing foreign language detection if you have forgotten some of the concepts.

In the second step, you will create word tokens from the Spanish reviews and will stem them using a SnowBall stemmer for the Spanish language. The language detection package is not perfect, unfortunately. Therefore, it is possible that sometimes the detected language is not correct.

Instructions 1/2
0 XP
Import the langdetect package.
Iterate over the rows of the non_english_reviews using the len() method and range() function.
Use detect_langs() to detect the language of each review in the for loop.

Instructions 2/2
0 XP
Import the SnowballStemmer from the respective package.
Create word tokens from the review column of the filtered_reviews from the previous step.
Use the Spanish stemmer you imported to stem the created list of tokens.
"""
# Import the required packages
from nltk.stem.snowball import SnowballStemmer
from nltk import word_tokenize
import pandas as pd

# Import the Spanish SnowballStemmer
# Import the language detection package
import langdetect
non_english_reviews=pd.read_csv("non_english_reviews.csv", encoding='latin-1')

# Loop over the rows of the dataset and append
languages = []
for i in range(len(non_english_reviews)):
    languages.append(langdetect.detect_langs(non_english_reviews.iloc[i, 1]))

# Clean the list by splitting
languages = [str(lang).split(':')[0][1:] for lang in languages]
# Assign the list to a new feature
non_english_reviews['language'] = languages

# Select the Spanish ones
filtered_reviews = non_english_reviews[non_english_reviews.language == 'es']




print("#################################################################")

SpanishStemmer = SnowballStemmer("spanish")

# Create a list of tokens
tokens = [word_tokenize(review) for review in filtered_reviews.review]
# Stem the list of tokens
stemmed_tokens = [[SpanishStemmer.stem(word) for word in token] for token in tokens]

# Print the first item of the stemmed tokenss
print(stemmed_tokens[0])