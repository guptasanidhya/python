"""Writing match patterns
In this exercise, you'll practice writing more complex match patterns using different token attributes and operators. A matcher is already initialized and available as the variable matcher.

Instructions 1/3
35 XP
1


Write one pattern that only matches mentions of the full iOS versions: "iOS 7", "iOS 11" and "iOS 10"."""

import spacy
# Load the 'en_core_web_sm' model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

doc = nlp("After making the iOS update you won't notice a radical system-wide redesign: nothing like the aesthetic upheaval we got with iOS 7. Most of iOS 11's furniture remains the same as in iOS 10. But you will discover some tweaks once you delve a little deeper.")

# Write a pattern for full iOS versions ("iOS 7", "iOS 11", "iOS 10")
pattern = [{'TEXT': "iOS"}, {'IS_DIGIT': True}]

# Add the pattern to the matcher and apply the matcher to the doc
# Add the pattern to the matcher
matcher.add('IPHONE_X_PATTERN', [pattern], on_match=None)

matches = matcher(doc)
print('Total matches found:', len(matches))

# Iterate over the matches and print the span text
for match_id, start, end in matches:
    print('Match found:', doc[start:end].text)