"""Writing match patterns
In this exercise, you'll practice writing more complex match patterns using different token attributes and operators. A matcher is already initialized and available as the variable matcher.

Instructions 1/3
35 XP
1


Write one pattern that only matches forms of "download" (tokens with the lemma "download"), followed by a token with the part-of-speech tag 'PROPN' (proper noun)."."""

import spacy
# Load the 'en_core_web_sm' model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

doc = nlp("i downloaded Fortnite on my laptop and can't open the game at all. Help? so when I was downloading Minecraft, I got the Windows version where it is the '.zip' folder and I used the default program to unpack it... do I also need to download Winzip?")

# Write a pattern that matches a form of "download" plus proper noun
# pattern = [{'LEMMA': 'download'}, {'POS': 'PROPN'}]
pattern = [{'LEMMA': 'download'}, {'POS': 'PROPN'}]
# Add the pattern to the matcher
matcher.add('DOWNLOAD_THINGS_PATTERN', [pattern], on_match=None)
matches = matcher(doc)
print('Total matches found:', len(matches))

# Iterate over the matches and print the span text
for match_id, start, end in matches:
    print('Match found:', doc[start:end].text)