from tensorflow import keras,Variable,estimator
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import feature_column
housing=pd.read_csv('../estimators_api/kc_house_data.csv')
# Define the targets and features
# Define feature columns for bedrooms and bathrooms
bedrooms = feature_column.numeric_column("bedrooms")
bathrooms = feature_column.numeric_column("bathrooms")
# Define the list of feature columns
feature_list = [bedrooms,bathrooms]

def input_fn():
	# Define the labels
	labels = np.array(housing['price'])
	# Define the features
	features = {'bedrooms':np.array(housing['bedrooms']),
                'bathrooms':np.array(housing['bathrooms'])}
	return features, labels


# Define the model and set the number of steps
"""In the previous exercise, you defined a list of feature columns, feature_list, and a data input function, input_fn(). In this exercise, you will build on that work by defining an estimator that makes use of input data."""
"""Use a deep neural network regressor with 2 nodes in both the first and second hidden layers and 1 training step."""
model = estimator.DNNRegressor(feature_columns=feature_list, hidden_units=[2,2])
model.train(input_fn, steps=1)

# Define the model and set the number of steps
"""Modify the code to use a LinearRegressor(), remove the hidden_units, and set the number of steps to 2."""
model = estimator.LinearRegressor(feature_columns=feature_list, )
model.train(input_fn, steps=2)
"""
Preparing to train with Estimators
For this exercise, we'll return to the King County housing transaction dataset from chapter 2. We will again develop and train a machine learning model to predict house prices; however, this time, we'll do it using the estimator API.

Rather than completing everything in one step, we'll break this procedure down into parts. We'll begin by defining the feature columns and loading the data. In the next exercise, we'll define and train a premade estimator. Note that feature_column has been imported for you from tensorflow. Additionally, numpy has been imported as np, and the Kings County housing dataset is available as a pandas DataFrame: housing.

"""

"""
Complete the feature column for bedrooms and add another numeric feature column for bathrooms. Use bedrooms and bathrooms as the keys.
Create a list of the feature columns, feature_list, in the order in which they were defined.
Set labels to be equal to the price column in housing.
Complete the bedrooms entry of the features dictionary and add another entry for bathrooms.
"""

"""Great work! Note that you have other premade estimator options, such as BoostedTreesRegressor(), and can also create your own custom estimators."""