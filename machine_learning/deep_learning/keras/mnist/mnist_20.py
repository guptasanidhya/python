# Import necessary modules
import numpy as np
import pandas as pd
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical


df=pd.read_csv('mnist.csv')
y=to_categorical(df.iloc[:,0])
print(df.info())
df.drop(columns=df.columns[0],
        axis=1,
        inplace=True)
x=df
# Create the model: model
model = Sequential()

# Add the first hidden layer
model.add(Dense(50, activation='relu', input_shape=(784,)))

# Add the second hidden layer
model.add(Dense(50, activation='relu'))

# Add the output layer
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Fit the model
model.fit(x, y, validation_split=0.3,epochs=10)

"""
Building your own digit recognition model
You've reached the final exercise of the course - you now know everything you need to build an accurate model to recognize handwritten digits!

We've already done the basic manipulation of the MNIST dataset shown in the video, so you have X and y loaded and ready to model with. Sequential and Dense from Keras are also pre-imported.

To add an extra challenge, we've loaded only 2500 images, rather than 60000 which you will see in some published results. Deep learning models perform better with more data, however, they also take longer to train, especially when they start becoming more complex.

If you have a computer with a CUDA compatible GPU, you can take advantage of it to improve computation time. If you don't have a GPU, no problem! You can set up a deep learning environment in the cloud that can run your models on a GPU. Here is a blog post by Dan that explains how to do this - check it out after completing this exercise! It is a great next step as you continue your deep learning journey.

Ready to take your deep learning to the next level? Check out Advanced Deep Learning with Keras to see how the Keras functional API lets you build domain knowledge to solve new types of problems. Once you know how to use the functional API, take a look at Image Processing with Keras in Python to learn image-specific applications of Keras.

Instructions
0 XP
Instructions
0 XP
Create a Sequential object to start your model. Call this model.
Add the first Dense hidden layer of 50 units to your model with 'relu' activation. For this data, the input_shape is (784,).
Add a second Dense hidden layer with 50 units and a 'relu' activation function.
Add the output layer. Your activation function should be 'softmax', and the number of nodes in this layer should be the same as the number of possible outputs in this case: 10.
Compile model as you have done with previous models: Using 'adam' as the optimizer, 'categorical_crossentropy' for the loss, and metrics=['accuracy'].
Fit the model using X and y using a validation_split of 0.3.

Hint
Assign Sequential() to model to start specifying the model.
Use the .add() method of model to add Dense layers with the appropriate number of units. Use the activation parameter to specify 'relu' as the activation function for the hidden layers and 'softmax' as the activation function for the output layer. Be sure to specify input_shape=(784,) for the first layer.
To compile your model, use model.compile() and specify the arguments mentioned in the instructions for the optimizer, loss, and metrics parameters.
To fit the model, use model.fit() with X as the first argument and y as the second argument. Use the validation_split parameter to specify the validation split to be 0.3.
"""


