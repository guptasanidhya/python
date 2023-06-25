"""
Word tokens from the Avengers
Now that you have tokenized your first string, it is time to iterate over items of a list and tokenize them as well. An easy way to do that with one line of code is with a list comprehension.

A list avengers has been created for you. It contains a few quotes from the Avengers movies. You can explore it in the IPython Shell.

Instructions
100 XP
Import the required function and package.
Apply the word tokenizing function on each item of our list.
"""
avengers=["Cause if we can't protect the Earth, you can be d*** sure we'll avenge it",
 'There was an idea to bring together a group of remarkable people, to see if we could become something more',
 "These guys come from legend, Captain. They're basically Gods."]
# Import the word tokenizing function
from nltk import word_tokenize

# Tokenize each item in the avengers
tokens_avengers = [word_tokenize(item) for item in avengers]

print(tokens_avengers)