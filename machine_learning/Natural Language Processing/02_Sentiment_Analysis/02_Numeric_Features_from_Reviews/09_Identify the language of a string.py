"""
Identify the language of a string
Sometimes you might need to analyze the sentiment of non-English text. Your first task in such a case will be to identify the foreign language.

In this exercise you will identify the language of a single string. A string called foreign has been created for you. It has been randomly extracted from the reviews dataset and may contain some grammatical errors. Feel free to explore it in the IPython Shell.

Instructions
100 XP
Import the required function from the language detection package.
Detect the language of the foreign string.
"""
# Import the language detection function and package
from langdetect import detect_langs
foreign="L'histoire rendu était fidèle, excellent, et grande."
# Detect the language of the foreign string
print(detect_langs(foreign))
