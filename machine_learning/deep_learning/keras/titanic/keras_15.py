# Import necessary modules
import numpy as np
import pandas as pd
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical
from keras.optimizers import SGD

df=pd.read_csv('titanic_all_numeric.csv')

x = np.asarray(df.survived).astype('float32')
predictors = df.drop(['survived','age_was_missing'], axis=1)
# print(predictors)
target = to_categorical(x)
n_cols = predictors.shape[1]

def get_new_model():
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape =(n_cols,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    return(model)
lr_to_test = [.000001, 0.01, 1]
# loop over learning rates
for lr in lr_to_test:
    model = get_new_model()
    my_optimizer = SGD(lr=lr)
    model.compile(optimizer = my_optimizer, loss = 'categorical_crossentropy')
    model.fit(predictors, target)
    print('fit')
"""
Changing optimization parameters
It's time to get your hands dirty with optimization. You'll now try optimizing a model at a very low learning rate, a very high learning rate, and a "just right" learning rate. You'll want to look at the results after running this exercise, remembering that a low value for the loss function is good.

For these exercises, we've pre-loaded the predictors and target values from your previous classification models (predicting who would survive on the Titanic). You'll want the optimization to start from scratch every time you change the learning rate, to give a fair comparison of how each learning rate did in your results. So we have created a function get_new_model() that creates an unoptimized model to optimize.

Instructions
0 XP
Instructions
0 XP
Import SGD from keras.optimizers.
Create a list of learning rates to try optimizing with called lr_to_test. The learning rates in it should be .000001, 0.01, and 1.
Using a for loop to iterate over lr_to_test:
Use the get_new_model() function to build a new, unoptimized model.
Create an optimizer called my_optimizer using the SGD() constructor with keyword argument lr=lr.
Compile your model. Set the optimizer parameter to be the SGD object you created above, and because this is a classification problem, use 'categorical_crossentropy' for the loss parameter.
Fit your model using the predictors and target.

Hint
Use the command from y import x to import x from y.
You can create a list containing a, b, and c using [a, b, c].
Inside the for loop:
Assign the result of get_new_model() to model and SGD(lr=lr) to my_optimizer.
To compile your model, use model.compile() and specify the arguments mentioned in the instructions for the optimizer and loss parameters.
Use model.fit() to fit your model, with predictors as the first argument and target as the second argument.
"""