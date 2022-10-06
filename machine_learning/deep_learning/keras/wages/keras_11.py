import numpy as np
import pandas as pd
# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential
df=pd.read_csv('hourly_wages.csv')
target = df['wage_per_hour'].values
x = df.drop('wage_per_hour', axis=1).values
predictors=np.matrix(x)

print(target)

# Save the number of columns in predictors: n_cols
n_cols = predictors.shape[1]
print(n_cols)
# Set up the model: model
model = Sequential()

# Add the first layer
model.add(Dense(50, activation='relu', input_shape=(n_cols,)))

# Add the second layer
model.add(Dense(32, activation='relu'))
# Add the output layer
model.add(Dense(1))
# Compile the model
model.compile(optimizer='adam',loss='mean_squared_error')

# Verify that model contains information from compiling
print("Loss function: " + model.loss)
# Fit the model
model.fit(predictors,target)
"""
Specifying a model
Now you'll get to work with your first model in Keras, and will immediately be able to run more complex neural network models on larger datasets compared to the first two chapters.

To start, you'll take the skeleton of a neural network and add a hidden layer and an output layer. You'll then fit that model and see Keras do the optimization so your model continually gets better.

As a start, you'll predict workers wages based on characteristics like their industry, education and level of experience. You can find the dataset in a pandas dataframe called df. For convenience, everything in df except for the target has been converted to a NumPy matrix called predictors. The target, wage_per_hour, is available as a NumPy matrix called target.

For all exercises in this chapter, we've imported the Sequential model constructor, the Dense layer constructor, and pandas.

Instructions
0 XP
Instructions
0 XP
Store the number of columns in the predictors data to n_cols. This has been done for you.
Start by creating a Sequential model called model.
Use the .add() method on model to add a Dense layer.
Add 50 units, specify activation='relu', and the input_shape parameter to be the tuple (n_cols,) which means it has n_cols items in each row of data, and any number of rows of data are acceptable as inputs.
Add another Dense layer. This should have 32 units and a 'relu' activation.
Finally, add an output layer, which is a Dense layer with a single node. Don't use any activation function here.

Hint
Assign Sequential() to model to start specifying the model.
Use the .add() method of model to add Dense layers with the appropriate number of units. Use the activation parameter to specify 'relu' as the activation function for the first and second layers. Be sure to specify input_shape=(n_cols,) for the first layer.
"""

"""
Compiling the model
You're now going to compile the model you specified earlier. To compile the model, you need to specify the optimizer and loss function to use. In the video, Dan mentioned that the Adam optimizer is an excellent choice. You can read more about it as well as other Keras optimizers here, and if you are really curious to learn more, you can read the original paper that introduced the Adam optimizer.

In this exercise, you'll use the Adam optimizer and the mean squared error loss function. Go for it!

Instructions
70 XP
Compile the model using model.compile(). Your optimizer should be 'adam' and the loss should be 'mean_squared_error'.


Show Answer (-70 XP)
Hint
To compile your model, use model.compile() and specify the arguments mentioned in the instructions for the optimizer, and loss parameters.
"""

"""
Fitting the model
You're at the most fun part. You'll now fit the model. Recall that the data to be used as predictive features is loaded in a NumPy matrix called predictors and the data to be predicted is stored in a NumPy matrix called target. Your model is pre-written and it has been compiled with the code from the previous exercise.

Instructions
100 XP
Fit the model. Remember that the first argument is the predictive features (predictors), and the data to be predicted (target) is the second argument.
"""