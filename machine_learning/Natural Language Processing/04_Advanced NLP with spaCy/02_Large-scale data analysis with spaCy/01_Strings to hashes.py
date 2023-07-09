"""Strings to hashes
The nlp object has already been created for you.

Instructions 1/2
50 XP
1
Look up the string "cat" in nlp.vocab.strings to get the hash.
Look up the hash to get back the string."""
# Look up the hash for the word "cat"

import spacy
# Load the 'en_core_web_sm' model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')
cat_hash = nlp.vocab.strings['cat']
print(cat_hash)

# Look up the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)