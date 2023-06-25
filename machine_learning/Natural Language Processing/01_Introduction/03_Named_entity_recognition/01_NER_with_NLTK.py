article='\ufeffThe taxi-hailing company Uber brings into very sharp focus the question of whether corporations can be said to have a moral character. If any human being were to behave with the single-minded and ruthless greed of the company, we would consider them sociopathic. Uber wanted to know as much as possible about the people who use its service, and those who don’t. It has an arrangement with unroll.me, a company which offered a free service for unsubscribing from junk mail, to buy the contacts unroll.me customers had had with rival taxi companies. Even if their email was notionally anonymised, this use of it was not something the users had bargained for. Beyond that, it keeps track of the phones that have been used to summon its services even after the original owner has sold them, attempting this with Apple’s phones even thought it is forbidden by the company.\r\n\r\n\r\nUber has also tweaked its software so that regulatory agencies that the company regarded as hostile would, when they tried to hire a driver, be given false reports about the location of its cars. Uber management booked and then cancelled rides with a rival taxi-hailing company which took their vehicles out of circulation. Uber deny this was the intention. The punishment for this behaviour was negligible. Uber promised not to use this “greyball” software against law enforcement – one wonders what would happen to someone carrying a knife who promised never to stab a policeman with it. Travis Kalanick of Uber got a personal dressing down from Tim Cook, who runs Apple, but the company did not prohibit the use of the app. Too much money was at stake for that.\r\n\r\n\r\nMillions of people around the world value the cheapness and convenience of Uber’s rides too much to care about the lack of drivers’ rights or pay. Many of the users themselves are not much richer than the drivers. The “sharing economy” encourages the insecure and exploited to exploit others equally insecure to the profit of a tiny clique of billionaires. Silicon Valley’s culture seems hostile to humane and democratic values. The outgoing CEO of Yahoo, Marissa Mayer, who is widely judged to have been a failure, is likely to get a $186m payout. This may not be a cause for panic, any more than the previous hero worship should have been a cause for euphoria. Yet there’s an urgent political task to tame these companies, to ensure they are punished when they break the law, that they pay their taxes fairly and that they behave responsibly.'
"""
NER with NLTK
You're now going to have some fun with named-entity recognition! A scraped news article has been pre-loaded into your workspace. Your task is to use nltk to find the named entities in this article.

What might the article be about, given the names you found?

Along with nltk, sent_tokenize and word_tokenize from nltk.tokenize have been pre-imported.

Instructions
100 XP
Instructions
100 XP
Tokenize article into sentences.
Tokenize each sentence in sentences into words using a list comprehension.
Inside a list comprehension, tag each tokenized sentence into parts of speech using nltk.pos_tag().
Chunk each tagged sentence into named-entity chunks using nltk.ne_chunk_sents(). Along with pos_sentences, specify the additional keyword argument binary=True.
Loop over each sentence and each chunk, and test whether it is a named-entity chunk by testing if it has the attribute label, and if the chunk.label() is equal to "NE". If so, print that chunk.
"""

from nltk import sent_tokenize,word_tokenize
import nltk
# nltk.download('averaged_perceptron_tagger', quiet=True)
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# Tokenize the article into sentences: sentences
sentences = sent_tokenize(article)

# Tokenize each sentence into words: token_sentences
token_sentences = [word_tokenize(sent) for sent in sentences]

# Tag each tokenized sentence into parts of speech: pos_sentences
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences]

# Create the named entity chunks: chunked_sentences
# chunked_sentences = nltk.ne_chunk_sents(pos_sentences,binary=False)
"""
Tree('PERSON', [('Jacinda', 'NNP'), ('Ardern', 'NNP')])
As you can see, Jacinda Ardern is chunked together and classified as a person.
 Also, note that the binary parameter in the ne_chunck has been set to ‘False’.If this parameter 
 is set to True, the output just points out the named entity as NE  instead of the type of named entity as shown below:
 Tree('NE', [('Jacinda', 'NNP'), ('Ardern', 'NNP')])
"""

# # Create the named entity chunks: chunked_sentences
chunked_sentences = nltk.ne_chunk_sents(pos_sentences,binary=True)

"""nltk.ne_chunk_sents() is a function from the NLTK library that performs named entity chunking on a list of sentences.
It takes the pos_sentences list, which contains POS-tagged sentences, as input.
The binary=False parameter indicates that named entities should be labeled with their specific entity types.
The function applies named entity recognition (NER) to each sentence and groups the recognized entities together, producing a parse tree for each sentence.
The resulting parse trees, representing the chunked sentences with identified named entities, are stored in the chunked_sentences object."""
# Test for stems of the tree with 'NE' tags
for sent in chunked_sentences:
    print(sent)
    for chunk in sent:
        if hasattr(chunk, "label") and chunk.label() == "NE":
            print(chunk)
