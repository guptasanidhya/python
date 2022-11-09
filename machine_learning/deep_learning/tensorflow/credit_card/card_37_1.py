from tensorflow import Variable,keras
import tensorflow as tf

# Initialize x_1 and x_2
x_1 = Variable(0.05,tf.float32)
x_2 = Variable(0.05,tf.float32)

# Define the optimization operation for opt_1 and opt_2
opt_1 = keras.optimizers.RMSprop(learning_rate=0.01, momentum=0.99)
opt_2 = keras.optimizers.RMSprop(learning_rate=0.01,momentum=0.00)

# for j in range(100):
	# opt_1.minimize(lambda: loss_function(x_1), var_list=[x_1])
    # # Define the minimization operation for opt_2
	# opt_2.minimize(lambda:loss_function(x_2), var_list=[x_2])

# Print x_1 and x_2 as numpy arrays
print(x_1.numpy(), x_2.numpy())

"""
Avoiding local minima
The previous problem showed how easy it is to get stuck in local minima. We had a simple optimization problem in one variable and gradient descent still failed to deliver the global minimum when we had to travel through local minima first. One way to avoid this problem is to use momentum, which allows the optimizer to break through local minima. We will again use the loss function from the previous problem, which has been defined and is available for you as loss_function().

Several optimizers in tensorflow have a momentum parameter, including SGD and RMSprop. You will make use of RMSprop in this exercise. Note that x_1 and x_2 have been initialized to the same value this time. Furthermore, keras.optimizers.RMSprop() has also been imported for you from tensorflow.
"""

"""
Set the opt_1 operation to use a learning rate of 0.01 and a momentum of 0.99.
Set opt_2 to use the root mean square propagation (RMS) optimizer with a learning rate of 0.01 and a momentum of 0.00.
Define the minimization operation for opt_2.
Print x_1 and x_2 as numpy arrays.
"""
"""
Good work! Recall that the global minimum is approximately 4.38. Notice that opt_1 built momentum, bringing x_1 closer to the global minimum. To the contrary, opt_2, which had a momentum parameter of 0.0, got stuck in the local minimum on the left
"""