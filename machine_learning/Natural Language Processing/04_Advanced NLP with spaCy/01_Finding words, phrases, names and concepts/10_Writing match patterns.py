"""Writing match patterns
In this exercise, you'll practice writing more complex match patterns using different token attributes and operators. A matcher is already initialized and available as the variable matcher.

Write one pattern that matches adjectives ('ADJ') followed by one or two 'NOUN's (one noun and one optional noun).
"""

import spacy
# Load the 'en_core_web_sm' model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

doc = nlp("Features of the app include a beautiful design, smart search, automatic labels and optional voice responses.")

# Write a pattern for adjective plus one or two nouns
pattern = [{'POS': 'ADJ'}, {'POS': 'NOUN'}, {'POS': 'NOUN', 'OP': '?'}]

# Add the pattern to the matcher and apply the matcher to the doc
matcher.add('ADJ_NOUN_PATTERN', [pattern], on_match=None)
matches = matcher(doc)
print('Total matches found:', len(matches))

# Iterate over the matches and print the span text
for match_id, start, end in matches:
    print('Match found:', doc[start:end].text)