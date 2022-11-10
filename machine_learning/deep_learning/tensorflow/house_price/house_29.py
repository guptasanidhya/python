from tensorflow import Variable,constant,keras
import numpy as np
import pandas as pd

housing=pd.read_csv('../estimators_api/kc_house_data.csv')
# Define the targets and features
price = np.array(housing['price'], np.float32)
price_log=np.log(price)
size = np.array(housing['sqft_living'], np.float32)
size_log=np.log(size)
# print(size_log)


# Define a linear regression model
def linear_regression(intercept, slope, features=size_log):
    return intercept + features * slope


# Set loss_function() to take the variables as arguments
def loss_function(intercept, slope, features=size_log, targets=price_log):
    # Set the predicted values
    predictions = linear_regression(intercept, slope, features)

    # Return the mean squared error loss
    return keras.losses.mse(targets, predictions)


# Compute the loss for different slope and intercept values
print(loss_function(0.1, 0.1).numpy())
print(loss_function(0.1, 0.5).numpy())


"""
Set up a linear regression
A univariate linear regression identifies the relationship between a single feature and the target tensor. In this exercise, we will use a property's lot size and price. Just as we discussed in the video, we will take the natural logarithms of both tensors, which are available as price_log and size_log.

In this exercise, you will define the model and the loss function. You will then evaluate the loss function for two different values of intercept and slope. Remember that the predicted values are given by intercept + features*slope. Additionally, note that keras.losses.mse() is available for you. Furthermore, slope and intercept have been defined as variables.

Instructions
0 XP
Instructions
0 XP
Define a function that returns the predicted values for a linear regression using intercept, features, and slope, and without using add() or multiply().
Complete the loss_function() by adding the model's variables, intercept and slope, as arguments.
Compute the mean squared error using targets and predictions.

Hint
Set linear_regression to return intercept + features*slope.
Use def to set the function's name to loss_function() and include the arguments in the order in which they were listed.
The mean squared error can be calculated with keras.losses.mse().
"""


"""
Great work! In the next exercise, you will actually run the regression and train intercept and slope.
"""