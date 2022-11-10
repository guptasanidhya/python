import numpy as np
import pandas as pd
from tensorflow import keras
import tensorflow as tf

# Assign the path to a string variable named data_path
data_path = '../estimators_api/kc_house_data.csv'

# Load the dataset as a dataframe named housing
housing = pd.read_csv(data_path)

# Print the price column of housing
print(housing['price'])

# Use a numpy array to define price as a 32-bit float
price = np.array(housing['price'], np.float32)

# Define waterfront as a Boolean using cast
waterfront = tf.cast(housing['waterfront'], tf.bool)

# Print price and waterfront
print(price)
print(waterfront)

#predictions=array([154546.51228417, 153942.9622033 ,  40833.26164156, ...,369047.72405433, 162293.96762846, 148248.92465109])

# Compute the mean squared error (mse)
# loss = keras.losses.mse(price, predictions)

# Print the mean squared error (mse)
# print(loss.numpy())
#ans=141171604777.12717

"""IN case of mae"""

# Compute the mean squared error (mae)
# loss = keras.losses.mae(price, predictions)

# Print the mean squared error (mae)
# print(loss.numpy())
# ans=268827.99302088


""" Great work! You may have noticed that the MAE was much smaller than the MSE, even though price and predictions were the same. This is because the different loss functions penalize deviations of predictions from price differently. MSE does not like large deviations and punishes them harshly."""

"""
Load data using pandas
Before you can train a machine learning model, you must first import data. There are several valid ways to do this, but for now, we will use a simple one-liner from pandas: pd.read_csv(). Recall from the video that the first argument specifies the path or URL. All other arguments are optional.

In this exercise, you will import the King County housing dataset, which we will use to train a linear model later in the chapter.

Instructions
100 XP
Import pandas under the alias pd.
Assign the path to a string variable with the name data_path.
Load the dataset as a pandas dataframe named housing.
Print the price column of housing.
"""


"""
Setting the data type
In this exercise, you will both load data and set its type. Note that housing is available and pandas has been imported as pd. You will import numpy and tensorflow, and define tensors that are usable in tensorflow using columns in housing with a given data type. Recall that you can select the price column, for instance, from housing using housing['price'].

Instructions
100 XP
Import numpy and tensorflow under their standard aliases.
Use a numpy array to set the tensor price to have a data type of 32-bit floating point number
Use the tensorflow function cast() to set the tensor waterfront to have a Boolean data type.
Print price and then waterfront. Did you notice any important differences?

"""

"""
Loss functions in TensorFlow
In this exercise, you will compute the loss using data from the King County housing dataset. You are given a target, price, which is a tensor of house prices, and predictions, which is a tensor of predicted house prices. You will evaluate the loss function and print out the value of the loss.

Instructions 1/2
35 XP
Import the keras module from tensorflow. Then, use price and predictions to compute the mean squared error (mse).
"""