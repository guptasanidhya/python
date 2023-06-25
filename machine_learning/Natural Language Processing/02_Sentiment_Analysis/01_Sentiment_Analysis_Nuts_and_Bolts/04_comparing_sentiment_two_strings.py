"""Comparing the sentiment of two strings
In this exercise, you will compare the sentiment of two different strings. A string called annak has been defined for you and it contains the first sentence of Anna Karenina. A second string called catcher has been created and it contains the first sentence of The Catcher in the Rye. Feel free to explore both in the IPython Shell.

Your task is again to detect the sentiment of each string - both their polarity and subjectivity. Which one has higher sentiment score? Did you expect that to be the case?

Instructions
100 XP
Import the required function from the appropriate package.
Create a text blob object from the annak string.
Create a text blob from the catcher string as well.
Print out the polarity and subjectivity of each of the created blobs."""
annak="Happy families are all alike; every unhappy family is unhappy in its own way"
catcher="If you really want to hear about it,the first thing you'll probably want to know is where I was born, and what my lousy childhood was like, and how my parents were occupied and all before they had me, and all that David Copperfield kind of crap, but I don't feel like going into it, if you want to know the truth."

# Import the required packages
from textblob import TextBlob

# Create a textblob object
blob_annak = TextBlob(annak)
blob_catcher = TextBlob(catcher)

# Print out the sentiment
print('Sentiment of annak: ', blob_annak.sentiment)
print('Sentiment of catcher: ', blob_catcher.sentiment)

