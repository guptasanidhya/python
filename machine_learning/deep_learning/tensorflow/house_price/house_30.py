from tensorflow import keras
import numpy as np
import pandas as pd
import tensorflow as tf

housing=pd.read_csv('kc_house_data.csv')
# Define the targets and features
price = np.array(housing['price'], np.float32)
price_log=np.log(price)
size = np.array(housing['sqft_living'], np.float32)
size_log=np.log(size)


# Define the intercept and slope
intercept = tf.Variable(5.0, np.float32)
slope = tf.Variable(0.001, np.float32)

# Define a linear regression model
def linear_regression(intercept, slope, features=size_log):
    return intercept + features * slope


# Set loss_function() to take the variables as arguments
def loss_function(intercept, slope, features=size_log, targets=price_log):
    # Set the predicted values
    predictions = linear_regression(intercept, slope, features)

    # Return the mean squared error loss
    return keras.losses.mse(targets, predictions)


# Initialize an Adam optimizer
opt = keras.optimizers.Adam(0.5)
for j in range(100):
# Apply minimize, pass the loss function, and supply the variables
	opt.minimize(lambda: loss_function(intercept, slope), var_list=[intercept, slope])

# Print every 10th value of the loss
	if j % 10 == 0:

		print(loss_function(intercept, slope).numpy())

# import matplotlib.pyplot as plt
# plt.scatter(size_log,price_log)
# plt.show()
"""
Train a linear model
In this exercise, we will pick up where the previous exercise ended. The intercept and slope, intercept and slope, have been defined and initialized. Additionally, a function has been defined, loss_function(intercept, slope), which computes the loss using the data and model variables.

You will now define an optimization operation as opt. You will then train a univariate linear model by minimizing the loss to find the optimal values of intercept and slope. Note that the opt operation will try to move closer to the optimum with each step, but will require many steps to find it. Thus, you must repeatedly execute the operation.

Instructions
100 XP
Initialize an Adam optimizer as opt with a learning rate of 0.5.
Apply the .minimize() method to the optimizer.
Pass loss_function() with the appropriate arguments as a lambda function to .minimize().
Supply the list of variables that need to be updated to var_list.
"""

"""
Excellent! Notice that we printed loss_function(intercept, slope) every 10th execution for 100 executions. Each time, the loss got closer to the minimum as the optimizer moved the slope and intercept parameters closer to their optimal values.
"""