"""Detect language of a list of strings
Now you will detect the language of each item in a list. A list called sentences has been created for you and it contains 3 sentences, each in a different language. They have been randomly extracted from the product reviews dataset.

Instructions
100 XP
Iterate over the sentences in the list.
Detect the language of each sentence and append the detected language to the empty list languages."""
from langdetect import detect_langs

languages = []
sentences=["L'histoire rendu était fidèle, excellent, et grande.",
 'Excelente muy recomendable.',
 'It had a leak from day one but the return and exchange process was very quick.']

# Loop over the sentences in the list and detect their language
for sentence in sentences:
    languages.append(detect_langs(sentence))

print('The detected languages are: ', languages)