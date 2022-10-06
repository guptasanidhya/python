from tensorflow import Variable,keras,random,ones,matmul
from sklearn.metrics import confusion_matrix
from random import random
import tensorflow as tf
import pandas as pd
import numpy as np

df =pd.read_csv('uci_credit_card.csv')
# print(df.columns)
default= df['default.payment.next.month'].values
borrower_features = df.drop(['default.payment.next.month','ID'], axis=1).values

# Define input data
inputs = np.array(borrower_features, np.float32)
# Define dense layer 1
dense1 = tf.keras.layers.Dense(32, activation='relu')(inputs)
# Define dense layer 2
dense2 = tf.keras.layers.Dense(16, activation='relu')(dense1)
# Apply dropout operation
dropout1 = tf.keras.layers.Dropout(0.25)(dense2)
# Define output layer
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(dropout1)

print(outputs)
