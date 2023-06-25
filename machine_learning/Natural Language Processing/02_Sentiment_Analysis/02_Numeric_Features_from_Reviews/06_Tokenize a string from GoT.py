"""Tokenize a string from GoT
A first standard step when working with text is to tokenize it, in other words, split a bigger string into individual strings, which are usually single words (tokens).

A string GoT has been created for you and it contains a quote from George R.R. Martin's Game of Thrones. Your task is to split it into individual tokens.

Instructions
100 XP
Import the word tokenizing function from nltk.
Transform the GoT string to word tokens."""
# Import the required function

GoT='Never forget what you are, for surely the world will not. Make it your strength. Then it can never be your weakness. Armour yourself in it, and it will never be used to hurt you.'

from nltk import word_tokenize

# Transform the GoT string to word tokens
print(word_tokenize(GoT))