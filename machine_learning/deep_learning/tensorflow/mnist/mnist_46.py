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
model=keras.Sequential()

# Define the first layer
model.add(keras.layers.Dense(1024,activation='relu',input_shape=(784,)))

# Add activation function to classifier
model.add(keras.layers.Dense(4, activation='softmax'))

# Finish the model compilation
model.compile(optimizer=keras.optimizers.Adam(lr=0.001),
              loss='categorical_crossentropy', metrics=['accuracy'])

# Complete the model fit operation
model.fit(sign_language_features, sign_language_labels, epochs=50, validation_split=0.5)

"""
Overfitting detection
In this exercise, we'll work with a small subset of the examples from the original sign language letters dataset. A small sample, coupled with a heavily-parameterized model, will generally lead to overfitting. This means that your model will simply memorize the class of each example, rather than identifying features that generalize to many examples.

You will detect overfitting by checking whether the validation sample loss is substantially higher than the training sample loss and whether it increases with further training. With a small sample and a high learning rate, the model will struggle to converge on an optimum. You will set a low learning rate for the optimizer, which will make it easier to identify overfitting.

Note that keras has been imported from tensorflow.
"""
"""
Excellent work! You may have noticed that the validation loss, val_loss, was substantially higher than the training loss, loss. Furthermore, if val_loss started to increase before the training process was terminated, then we may have overfitted. When this happens, you will want to try decreasing the number of epochs.
"""

"""
Great job! Notice that the gap between the test and train set losses is high for large_model, suggesting that overfitting may be an issue. Furthermore, both test and train set performance is better for large_model. This suggests that we may want to use large_model, but reduce the number of training epochs.
"""