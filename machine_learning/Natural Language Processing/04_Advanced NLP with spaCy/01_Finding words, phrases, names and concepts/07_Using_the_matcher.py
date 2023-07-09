"""Using the Matcher
Let's try spaCy's rule-based Matcher. You'll be using the example from the previous exercise and write a pattern that can match the phrase "iPhone X" in the text. The nlp object and a processed doc are already available."""

# Import the Matcher and initialize it with the shared vocabulary

import spacy
# Load the 'en_core_web_sm' model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')

text = "New iPhone X release date leaked as Apple reveals pre-orders by mistake"

# Process the text
doc = nlp(text)


"""Instructions 1/3
35 XP
Import the Matcher from spacy.matcher.
Initialize it with the nlp object's shared vocab."""
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]

# Add the pattern to the matcher
matcher.add('IPHONE_X_PATTERN', [pattern], on_match=None)

# Use the matcher on the doc
matches = matcher(doc)

# Iterate over the matches and get the matched span from the start to the end index
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print('Matched span:', matched_span.text)