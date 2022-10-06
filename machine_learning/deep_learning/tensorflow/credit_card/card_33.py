from tensorflow import Variable,ones,matmul,keras
import numpy as np
import tensorflow as tf
borrower_features=Variable([[ 3.,  3., 23.],
       [ 2.,  1., 24.],
       [ 1.,  1., 49.],
       [ 1.,  1., 49.],
       [ 2.,  1., 29.]],tf.float32)

# Initialize bias1
bias1 = Variable(0.1)

# Initialize weights1 as 3x2 variable of ones
# weights1 = Variable(ones((3, 2)))
weights1=Variable([[-0.6 ,  0.6 ],
       [ 0.8 , -0.3 ],
       [-0.09, -0.08]],tf.float32)

# Compute the product of borrower_features and weights1
products1 = matmul(borrower_features,weights1)

# Apply a sigmoid activation function to products1 + bias1
dense1 = keras.activations.sigmoid(products1+bias1)

# Print the shapes of borrower_features, weights1, bias1, and dense1
print('\n shape of borrower_features: ', borrower_features.shape)
print('\n shape of weights1: ', weights1.shape)
print('\n shape of bias1: ', bias1.shape)
print('\n shape of dense1: ', dense1.shape)

"""
The low-level approach with multiple examples
In this exercise, we'll build further intuition for the low-level approach by constructing the first dense hidden layer for the case where we have multiple examples. We'll assume the model is trained and the first layer weights, weights1, and bias, bias1, are available. We'll then perform matrix multiplication of the borrower_features tensor by the weights1 variable. Recall that the borrower_features tensor includes education, marital status, and age. Finally, we'll apply the sigmoid function to the elements of products1 + bias1, yielding dense1.

 
 
products1=[33232124114911492129][−0.60.60.8−0.3−0.09−0.08]

Note that matmul() and keras() have been imported from tensorflow.

Instructions
70 XP
Instructions
70 XP
Compute products1 by matrix multiplying the features tensor by the weights.
Use a sigmoid activation function to transform products1 + bias1.
Print the shapes of borrower_features, weights1, bias1, and dense1.The low-level approach with multiple examples
In this exercise, we'll build further intuition for the low-level approach by constructing the first dense hidden layer for the case where we have multiple examples. We'll assume the model is trained and the first layer weights, weights1, and bias, bias1, are available. We'll then perform matrix multiplication of the borrower_features tensor by the weights1 variable. Recall that the borrower_features tensor includes education, marital status, and age. Finally, we'll apply the sigmoid function to the elements of products1 + bias1, yielding dense1.

 
 
products1=[33232124114911492129][−0.60.60.8−0.3−0.09−0.08]

Note that matmul() and keras() have been imported from tensorflow.

Instructions
70 XP
Instructions
70 XP
Compute products1 by matrix multiplying the features tensor by the weights.
Use a sigmoid activation function to transform products1 + bias1.
Print the shapes of borrower_features, weights1, bias1, and dense1.
"""

"""
Good job! Note that our input data, borrower_features, is 5x3 because it consists of 5 examples for 3 features. The shape of weights1 is 3x2, as it was in the previous exercise, since it does not depend on the number of examples. Additionally, bias1 is a scalar. Finally, dense1 is 5x2, which means that we can multiply it by the following set of weights, weights2, which we defined to be 2x1 in the previous exercise.
"""