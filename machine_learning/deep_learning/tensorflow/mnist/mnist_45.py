from tensorflow import keras
import tensorflow as tf
import pandas as pd
from keras.utils import to_categorical
from sklearn.preprocessing import MinMaxScaler
df=pd.read_csv('slmnist.csv')

sign_language_labels=to_categorical(df.iloc[:,0])#to_categorical makes the value categorical like 0,1 for all the outputs

scaler = MinMaxScaler()#scaled the images via 255 (normalization)
df.drop(columns=df.columns[0],axis=1,inplace=True)
scaled = scaler.fit_transform(df)

sign_language_features=scaled


# Define sequential model
model = keras.Sequential()

# Define the first layer
model.add(keras.layers.Dense(32, activation='sigmoid', input_shape=(784,)))

# Add activation function to classifier
model.add(keras.layers.Dense(4, activation='softmax'))

# Set the optimizer, loss function, and metrics
model.compile(optimizer='RMSprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Add the number of epochs and the validation split
model.fit(sign_language_features, sign_language_labels, epochs=10, validation_split=0.1)
"""
Metrics and validation with Keras
We trained a model to predict sign language letters in the previous exercise, but it is unclear how successful we were in doing so. In this exercise, we will try to improve upon the interpretability of our results. Since we did not use a validation split, we only observed performance improvements within the training set; however, it is unclear how much of that was due to overfitting. Furthermore, since we did not supply a metric, we only saw decreases in the loss function, which do not have any clear interpretation.

Note that keras has been imported for you from tensorflow.
"""
"""

"""