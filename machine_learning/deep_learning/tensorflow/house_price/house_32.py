# Import tensorflow, pandas, and numpy
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
# Define trainable variables
intercept = tf.Variable(10.0, tf.float32)
slope = tf.Variable(0.5, tf.float32)


# Define the model
def linear_regression(intercept, slope, features):
    # Define the predicted values
    return intercept + slope * features


# Define the loss function
def loss_function(intercept, slope, targets, features):
    # Define the predicted values
    predictions = linear_regression(intercept, slope, features)

    # Define the MSE loss
    return keras.losses.mse(targets, predictions)

# Initialize Adam optimizer
opt = keras.optimizers.Adam()

# Load data in batches
for batch in pd.read_csv('../estimators_api/kc_house_data.csv', chunksize=100):
	size_batch = np.array(batch['sqft_lot'], np.float32)

	# Extract the price values for the current batch
	price_batch = np.array(batch['price'], np.float32)

	# Complete the loss, fill in the variable list, and minimize
	opt.minimize(lambda: loss_function(intercept, slope, price_batch, size_batch), var_list=[intercept, slope])

# Print trained parameters
print(intercept.numpy(), slope.numpy())

"""
Preparing to batch train
Before we can train a linear model in batches, we must first define variables, a loss function, and an optimization operation. In this exercise, we will prepare to train a model that will predict price_batch, a batch of house prices, using size_batch, a batch of lot sizes in square feet. In contrast to the previous lesson, we will do this by loading batches of data using pandas, converting it to numpy arrays, and then using it to minimize the loss function in steps.

Variable(), keras(), and float32 have been imported for you. Note that you should not set default argument values for either the model or loss function, since we will generate the data in batches during the training process.

Instructions
100 XP
Instructions
100 XP
Define intercept as having an initial value of 10.0 and a data type of 32-bit float.
Define the model to return the predicted values using intercept, slope, and features.
Define a function called loss_function() that takes intercept, slope, targets, and features as arguments and in that order. Do not set default argument values.
Define the mean squared error loss function using targets and predictions.
"""

"""
Training a linear model in batches
In this exercise, we will train a linear regression model in batches, starting where we left off in the previous exercise. We will do this by stepping through the dataset in batches and updating the model's variables, intercept and slope, after each step. This approach will allow us to train with datasets that are otherwise too large to hold in memory.

Note that the loss function,loss_function(intercept, slope, targets, features), has been defined for you. Additionally, keras has been imported for you and numpy is available as np. The trainable variables should be entered into var_list in the order in which they appear as loss function arguments.

Instructions
100 XP
Instructions
100 XP
Use the .Adam() optimizer.
Load in the data from 'kc_house_data.csv' in batches with a chunksize of 100.
Extract the price column from batch, convert it to a numpy array of type 32-bit float, and assign it to price_batch.
Complete the loss function, fill in the list of trainable variables, and perform minimization.
"""