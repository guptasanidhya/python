from tensorflow import Variable,keras,random,ones,matmul
from sklearn.metrics import confusion_matrix
from random import random
import tensorflow as tf

# Define the layer 1 weights
w1 = Variable([[ 2.4435377 ,  0.6532978 , -2.0876322 , -0.6465399 ,  0.50398946,
        -0.6622369 ,  2.248099  ],
       [-0.6057031 , -0.74135935,  2.5471828 ,  2.9152145 , -1.3031693 ,
         0.8121961 , -0.06042745],
       [-1.4342147 ,  1.987995  ,  0.46523282,  1.1759586 ,  0.43213284,
        -0.3314867 ,  0.3673103 ],
       [-2.0169213 ,  0.75370973,  2.0362077 , -0.9722697 , -0.90286547,
        -0.46412855,  0.73538285],
       [ 0.4028158 , -1.0634764 , -0.69183266,  1.0082972 , -0.1223945 ,
        -0.67528254, -1.3772862 ],
       [ 0.09137809, -0.7528797 , -0.16444235,  0.257028  , -0.81907284,
         1.4698758 , -0.9347897 ],
       [ 0.26381123, -0.9540834 ,  0.52078825, -0.8119896 ,  0.03201316,
         2.0273645 , -1.6015768 ],
       [-0.13008343,  0.75125885, -1.1612765 , -0.19919561, -0.10818551,
         1.4675983 , -0.5593607 ],
       [-0.63245237,  3.5221422 ,  0.51096684, -0.5864398 ,  0.9112978 ,
         0.34698516,  0.68189377],
       [ 0.41752422,  0.7064977 , -1.0978483 , -0.7023961 ,  0.79573596,
         0.5765105 ,  0.5866237 ],
       [ 0.44239658,  0.06016769,  1.5716101 ,  0.65556014,  0.76095665,
         0.5687989 ,  1.1920937 ],
       [-0.68715763, -0.1728628 ,  1.4736586 , -0.4240413 ,  0.48358986,
         0.8436072 , -0.14853318],
       [ 1.6009874 ,  0.41357717,  0.68890846,  0.83247167, -0.00393822,
         0.29737377,  0.20552601],
       [-1.137845  , -0.02462507,  0.7824456 ,  1.013908  ,  1.3491129 ,
         1.552934  , -0.12183756],
       [-0.3266763 ,  2.2627    ,  1.4670117 , -0.6878452 , -0.5917342 ,
        -0.5329395 , -0.20593391],
       [ 0.55576605,  2.364314  ,  1.6994927 , -0.724152  , -0.2852429 ,
         0.1478058 , -0.80708194],
       [ 1.618923  ,  0.14479114, -1.111939  ,  0.16476874,  1.1102928 ,
        -1.3003356 ,  0.14524043],
       [ 0.8061737 ,  0.65021497,  1.404869  ,  2.3160765 , -0.5442242 ,
        -0.5231445 ,  0.90839577],
       [-0.14611603, -0.8277071 ,  0.66987085,  0.09163713, -0.33766454,
         2.1436663 ,  0.4740364 ],
       [-0.40199128,  0.86705554, -2.1632981 , -0.3115556 , -0.98251456,
        -0.10797349,  1.6352255 ],
       [ 0.23678602,  0.51027703, -1.8715134 , -0.66790223,  0.21952134,
         0.4172406 , -1.2710783 ],
       [-0.02490104, -0.5918932 ,  1.2865447 , -0.04981803, -1.7857966 ,
        -0.2095459 , -1.2845048 ],
       [-0.5743803 , -0.14933696, -2.2613177 , -1.0723772 ,  2.3046598 ,
        -1.5037003 ,  0.6880282 ]],tf.float32)

# Initialize the layer 1 bias
b1 = Variable([-0.7341992 , -0.38519704, -0.9991661 , -0.42893964,  0.86850995,
        2.714162  ,  1.475798  ],tf.float32)

# Define the layer 2 weights
w2 = Variable([[ 0.8205525 ],
       [ 0.41013834],
       [-1.1908278 ],
       [-1.5474229 ],
       [ 0.8174632 ],
       [-1.4407537 ],
       [-0.9222677 ]],tf.float32)

# Define the layer 2 bias
b2 = Variable([-1.2979275],tf.float32)

import pandas as pd

df =pd.read_csv('uci_credit_card.csv')
# print(df.columns)
default= df['default.payment.next.month'].values
borrower_features = df.drop(['default.payment.next.month','ID'], axis=1).values
# Define the model
def model(w1, b1, w2, b2, features = borrower_features):
	# Apply relu activation functions to layer 1
	layer1 = keras.activations.relu(matmul(features, w1) + b1)
    # Apply dropout rate of 0.25
	dropout = keras.layers.Dropout(0.25)(layer1)
	return keras.activations.sigmoid(matmul(dropout, w2) + b2)

# Define the loss function
def loss_function(w1, b1, w2, b2, features = borrower_features, targets = default):
	predictions = model(w1, b1, w2, b2)
	# Pass targets and predictions to the cross entropy loss
	return keras.losses.binary_crossentropy(targets, predictions)


test_features=borrower_features[:100]
test_targets=default[:100]

opt = keras.optimizers.RMSprop(learning_rate=0.01, momentum=0.99)
# Train the model
for j in range(100):
    # Complete the optimizer
	opt.minimize(lambda: loss_function(w1, b1, w2, b2),
                 var_list=[w1, b1, w2, b2])

# Make predictions with model using test features
model_predictions = model(w1, b1, w2, b2, test_features)

# Construct the confusion matrix
confusion_matrix(test_targets, model_predictions)
"""A good initialization can reduce the amount of time needed to find the global minimum. In this exercise, we will initialize weights and biases for a neural network that will be used to predict credit card default decisions. To build intuition, we will use the low-level, linear algebraic approach, rather than making use of convenience functions and high-level keras operations. We will also expand the set of input features from 3 to 23. Several operations have been imported from tensorflow: Variable(), random(), and ones().

Instructions
70 XP
Initialize the layer 1 weights, w1, as a Variable() with shape [23, 7], drawn from a normal distribution.
Initialize the layer 1 bias using ones.
Use a draw from the normal distribution to initialize w2 as a Variable() with shape [7, 1].
Define b2 as a Variable() and set its initial value to 0.0."""

"""
Nice work! One of the benefits of using tensorflow is that you have the option to customize models down to the linear algebraic-level, as we've shown in the last two exercises. If you print w1, you can see that the objects we're working with are simply tensors.
"""

"""
Nice work! The diagram shown is called a ``confusion matrix.'' The diagonal elements show the number of correct predictions. The off-diagonal elements show the number of incorrect predictions. We can see that the model performs reasonably-well, but does so by overpredicting non-default. This suggests that we may need to train longer, tune the model's hyperparameters, or change the model's architecture.


"""