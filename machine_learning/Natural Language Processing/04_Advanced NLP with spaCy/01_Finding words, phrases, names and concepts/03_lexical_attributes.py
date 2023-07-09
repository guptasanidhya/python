"""In this example, you'll use spaCy's Doc and Token objects, and lexical attributes to find percentages in a text. You'll be looking for two subsequent tokens: a number and a percent sign. The English nlp object has already been created.

Instructions
100 XP
Use the like_num token attribute to check whether a token in the doc resembles a number.
Get the token following the current token in the document. The index of the next token in the doc is token.i + 1.
Check whether the next token's text attribute is a percent sign "%"."""

# Import the English language class and create the nlp object
from spacy.lang.en import English
nlp = English()

# Process the text
doc = nlp("In 1990, more than 60% of people in East Asia were in extreme poverty. Now less than 4% are.")

# Iterate over the tokens in the doc
for token in doc:
    # Check if the token resembles a number
    if token.like_num:
        # Get the next token in the document
        next_token = doc[token.i+1]
        # Check if the next token's text equals '%'
        if next_token.text == '%':
            print('Percentage found:', token.text)