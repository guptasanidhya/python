two_cities="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."
"""
Detecting the sentiment of Tale of Two Cities
In the video we saw that one type of algorithms for detecting the sentiment are based on a lexicon of predefined words and their corresponding polarity score. Your task in this exercise is to detect the sentiment, including polarity and subjectivity of a given string using such a rule-based approach and the textblob library in Python.

You will work with the two_cities string. It contains the first sentence of Dickens's A Tale of Two Cities novel. Feel free to explore it in the Shell.

Instructions
100 XP
Create a text blob object from the two_cities string.
Print out the polarity and subjectivity.
"""

"""TextBlob returns polarity and subjectivity of a sentence. Polarity lies between [-1,1], -1 defines a negative
 sentiment and 1 defines a positive sentiment. Negation words reverse the polarity. TextBlob has semantic labels
  that help with fine-grained analysis. For example — emoticons, exclamation mark, emojis, etc. Subjectivity lies
   between [0,1]. Subjectivity quantifies the amount of personal opinion and factual information contained in the text.
    The higher subjectivity means that the text contains personal opinion rather than factual information. """
# Import the required packages
from textblob import TextBlob

# Create a textblob object
blob_two_cities = TextBlob(two_cities)

# Print out the sentiment
print(blob_two_cities.sentiment)
