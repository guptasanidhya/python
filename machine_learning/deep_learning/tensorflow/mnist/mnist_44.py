from tensorflow import keras
import tensorflow as tf
import pandas as pd
from keras.utils import to_categorical
df=pd.read_csv('slmnist.csv')

sign_language_labels=to_categorical(df.iloc[:,0])#to_categorical makes the value categorical like 0,1 for all the outputs
df.drop(columns=df.columns[0],axis=1,inplace=True)
sign_language_features=df

# Define a sequential model
model=keras.Sequential()

# Define a hidden layer
model.add(keras.layers.Dense(16, activation='relu', input_shape=(784,)))

# Define the output layer
model.add(keras.layers.Dense(4,activation='softmax'))
# Compile the model
model.compile('SGD', loss='categorical_crossentropy')

# Complete the fitting operation
model.fit(sign_language_features, sign_language_labels, epochs=5)

"""In this exercise, we return to our sign language letter classification problem. We have 2000 images of four letters--A, B, C, and D--and we want to classify them with a high level of accuracy. We will complete all parts of the problem, including the model definition, compilation, and training.

Note that keras has been imported from tensorflow for you. Additionally, the features are available as sign_language_features and the targets are available as sign_language_labels."""

"""
Great work! You probably noticed that your only measure of performance improvement was the value of the loss function in the training sample, which is not particularly informative. You will improve on this in the next exercise.
"""