"""Predicting linguistic annotations
You'll now get to try one of spaCy's pre-trained model packages and see its predictions in action. Feel free to try it out on your own text! The small English model is already available as the variable nlp.

To find out what a tag or label means, you can call spacy.explain in the IPython shell. For example: spacy.explain('PROPN') or spacy.explain('GPE').

Instructions 1/2
50 XP
1
2
Process the text with the nlp object and create a doc.
For each token, print the token text, the token's .pos_ (part-of-speech tag) and the token's .dep_ (dependency label)."""

import spacy
# Load the 'en_core_web_sm' model – spaCy is already imported
nlp = spacy.load('en_core_web_sm')

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

for token in doc:
    # Get the token text, part-of-speech tag and dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # This is for formatting only
    print('{:<12}{:<10}{:<10}'.format(token_text, token_pos, token_dep))


# Iterate over the predicted entities
for ent in doc.ents:
    # print the entity text and its label
    print(ent.text, ent.label_)