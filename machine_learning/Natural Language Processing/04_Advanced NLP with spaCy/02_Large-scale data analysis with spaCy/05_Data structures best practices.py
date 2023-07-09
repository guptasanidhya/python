"""Data structures best practices
The code in this example is trying to analyze a text and collect all proper nouns. If the token following the proper noun is a verb, it should also be extracted. A doc object has already been created.

# Get all tokens and part-of-speech tags
pos_tags = [token.pos_ for token in doc]

for index, pos in enumerate(pos_tags):
    # Check if the current token is a proper noun
    if pos == 'PROPN':
        # Check if the next token is a verb
        if pos_tags[index + 1] == 'VERB':
            print('Found a verb after a proper noun!')

Instructions 1/2
50 XP
Question
Why is the code bad?
Possible answers
It only uses lists of strings instead of native token attributes.This is often less efficient,
and can't express complex relationships
Instructions 2/2
0 XP
Rewrite the code to use the native token attributes instead of a list of pos_tags.
Loop over each token in the doc and check the token.pos_ attribute.
Use doc[token.i + 1] to check for the next token and its .pos_ attribute."""
import spacy
nlp=spacy.load("en_core_web_sm")

doc=nlp("Berlin is a nice city")
print(doc)
for token in doc:
    # Check if the current token is a proper noun
    if token.pos_ == 'PROPN':
        # Check if the next token is a verb
        if doc[token.i+1].pos_ == 'VERB':
            print('Found a verb after a proper noun!')