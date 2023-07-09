import pandas as pd
import numpy as np
import spacy
train_data=pd.read_csv('../02_understanding_natural_language/atis/atis_intents_train.csv')
# print(train_data)
sentences_train=train_data.iloc[:,1].tolist()
nlp=spacy.load('en_core_web_sm')

X_train_shape = (len(sentences_train),nlp.vocab.vectors_length)
X_train = np.zeros(X_train_shape)
for i,sentence in enumerate(sentences_train):
    X_train[i,:] = nlp(sentence).vector