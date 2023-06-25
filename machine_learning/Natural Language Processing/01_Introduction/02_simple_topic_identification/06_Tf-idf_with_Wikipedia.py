import itertools
from collections import defaultdict

from gensim.corpora.dictionary import Dictionary
from gensim.models import TfidfModel
from nltk.tokenize import word_tokenize
my_documents=['the movie was about spaceship and an alien','i really liked the movie','the spaceship was so cool','I wish i have a spaceship',"the aliens destroyed a lot of good spaceship"]
tokenized_docs=[word_tokenize(doc.lower()) for doc in my_documents]
articles=tokenized_docs
# Create a Dictionary from the articles: dictionary
dictionary = Dictionary(articles)
print(dictionary.token2id)
# Select the id for "computer": computer_id
spaceship_id = dictionary.token2id.get("spaceship")
print(spaceship_id)
# Use spaceship_id with the dictionary to print the word
print(dictionary.get(spaceship_id))


# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]
print(corpus)
total_word_count=defaultdict(int)
for word_id,word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id]+=word_count
sorted_word_count = sorted(total_word_count.items(), key=lambda w: w[1], reverse=True)

# doc=corpus[4]

"""Tf-idf with Wikipedia
Now it's your turn to determine new significant terms for your corpus by applying gensim's tf-idf. You will again have access to the same corpus and dictionary objects you created in the previous exercises - dictionary, corpus, and doc. Will tf-idf make for more interesting results on the document level?

TfidfModel has been imported for you from gensim.models.tfidfmodel.

Instructions 1/2
50 XP
Initialize a new TfidfModel called tfidf using corpus.
Use doc to calculate the weights. You can do this by passing [doc] to tfidf.
Print the first five term ids with weights."""
# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[sorted_word_count]
# tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

"""Sort the term ids and weights in a new list from highest to lowest weight. This has been done for you.
Using your pre-existing dictionary, print the top five weighted words (term_id) from sorted_tfidf_weights, along with their weighted score (weight)."""
# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id),weight)