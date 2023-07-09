"""Comparing similarities
In this exercise, you'll be using spaCy's similarity methods to compare Doc, Token and Span objects and get similarity scores. The medium English model is already available as the nlp object."""

import spacy
nlp=spacy.load('en_core_web_lg')

doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

# Get the similarity of doc1 and doc2
similarity = doc1.similarity(doc2)
print(similarity)

doc = nlp("TV and books")
token1, token2 = doc[0], doc[2]

# Get the similarity of the tokens "TV" and "books"
similarity = token1.similarity(token2)
print(similarity)

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Create spans for "great restaurant" and "really nice bar"
span1 = doc[3:5]
span2 = doc[-4:-1]

# Get the similarity of the spans
similarity = span1.similarity(span2)
print(similarity)