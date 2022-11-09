from tensorflow import Variable,ones,matmul,keras,constant
import numpy as np
import tensorflow as tf
import pandas as pd

# Initialize x_1 and x_2
x_1 = Variable(6.0,tf.float32)
x_2 = Variable(0.3,tf.float32)

# Define the optimization operation
opt = keras.optimizers.SGD(learning_rate=0.01)

# for j in range(100):
    # Perform minimization using the loss function and x_1
	# opt.minimize(lambda: loss_function(x_1), var_list=[x_1])
	# # Perform minimization using the loss function and x_2
	# opt.minimize(lambda: loss_function(x_2), var_list=[x_2])

# Print x_1 and x_2 as numpy arrays
print(x_1.numpy(), x_2.numpy())
"""4.3801394 0.42052683"""
"""
The dangers of local minima
Consider the plot of the following loss function, loss_function(), which contains a global minimum, marked by the dot on the right, and several local minima, including the one marked by the dot on the left.

The graph is of a single variable function that contains multiple local minima and a global minimum.

In this exercise, you will try to find the global minimum of loss_function() using keras.optimizers.SGD(). You will do this twice, each time with a different initial value of the input to loss_function(). First, you will use x_1, which is a variable with an initial value of 6.0. Second, you will use x_2, which is a variable with an initial value of 0.3. Note that loss_function() has been defined and is available.

Instructions
70 XP
Instructions
70 XP
Set opt to use the stochastic gradient descent optimizer (SGD) with a learning rate of 0.01.
Perform minimization using the loss function, loss_function(), and the variable with an initial value of 6.0, x_1.
Perform minimization using the loss function, loss_function(), and the variable with an initial value of 0.3, x_2.
Print x_1 and x_2 as numpy arrays and check whether the values differ. These are the minima that the algorithm identified.


Show Answer (-70 XP)
Hint
Use the keras.optimizers.SGD(learning_rate=r) operation, where r is the learning rate.
Pass x_1 as the only argument to the loss function and also to the variables list.
Remember to pass loss_function(x_2) to the minimize operation.
Apply .numpy() to x_1 and x_2 and pass them to the print() function.
"""

"""
Great work! Notice that we used the same optimizer and loss function, but two different initial values. When we started at 6.0 with x_1, we found the global minimum at 4.38, marked by the dot on the right. When we started at 0.3, we stopped around 0.42 with x_2, the local minimum marked by a dot on the far left.
"""