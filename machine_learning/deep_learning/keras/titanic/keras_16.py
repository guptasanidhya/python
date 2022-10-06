# Import necessary modules
import numpy as np
import pandas as pd
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical


df=pd.read_csv('titanic_all_numeric.csv')

x = np.asarray(df.survived).astype('float32')
predictors = df.drop(['survived','age_was_missing'], axis=1)
# print(predictors)
target = to_categorical(x)

n_cols = predictors.shape[1]
# Set up the model
model = Sequential()
model.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

# Fit the model
hist = model.fit(predictors,target,validation_split=0.3)

"""
Evaluating model accuracy on validation dataset
Now it's your turn to monitor model accuracy with a validation data set. A model definition has been provided as model. Your job is to add the code to compile it and then fit it. You'll check the validation score in each epoch.

Instructions
70 XP
Compile your model using 'adam' as the optimizer and 'categorical_crossentropy' for the loss. To see what fraction of predictions are correct (the accuracy) in each epoch, specify the additional keyword argument metrics=['accuracy'] in model.compile().
Fit the model using the predictors and target. Create a validation split of 30% (or 0.3). This will be reported in each epoch.
"""
