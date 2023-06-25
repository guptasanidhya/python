import itertools
from collections import defaultdict

from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.corpora.dictionary import Dictionary
my_documents=['the movie was about spaceship and an alien','i really liked the movie','the spaceship was so cool','I wish i have a spaceship',"the aliens destroyed a lot of good spaceship"]

tokens=[word_tokenize(doc.lower()) for doc in my_documents]
no_stops=[t for t in tokens if t not in stopwords.words('English')]
# print(no_stops)
dictionary=Dictionary(no_stops)

print(dictionary.token2id)
corpus=[dictionary.doc2bow(doc) for doc in no_stops]
# print(corpus)
doc=corpus[3]
bow_doc=sorted(doc,key=lambda w:w[1],reverse=True)
# print(bow_doc)

for word_id ,word_count in bow_doc[:5]:
    print(dictionary.get((word_id)),word_count)
print("____________________________________________________________________")
total_word_count=defaultdict(int)
for word_id,word_count in itertools.chain.from_iterable(corpus):
    total_word_count[word_id]+=word_count

# print(total_word_count)

sorted_word_count=sorted(total_word_count.items(),key=lambda w:w[1],reverse=True)
print(sorted_word_count)
for word_id,word_count in sorted_word_count[:5]:
    print(dictionary.get(word_id),word_count)