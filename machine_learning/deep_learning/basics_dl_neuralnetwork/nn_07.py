"""
Calculating slopes
You're now going to practice calculating slopes. When plotting the mean-squared error loss function against predictions, the slope is 2 * x * (xb-y), or 2 * input_data * error. Note that x and b may have multiple numbers (x is a vector for each data point, and b is a vector). In this case, the output will also be a vector, which is exactly what you want.

You're ready to write the code to calculate this slope while using a single data point. You'll use pre-defined weights called weights as well as data for a single point called input_data. The actual value of the target you want to predict is stored in target.

Instructions
0 XP
Calculate the predictions, preds, by multiplying weights by the input_data and computing their sum.
Calculate the error, which is preds minus target. Notice that this error corresponds to xb-y in the gradient expression.
Calculate the slope of the loss function with respect to the prediction. To do this, you need to take the product of input_data and error and multiply that by 2.

Hint
You can multiply arrays a and b and take their sum using (a * b).sum().
From preds, subtract target to calculate the error.
To calculate the slope, you need to take the product of 2, input_data, and error.
"""

import numpy as np
# The data point you will make a prediction for
input_data = np.array([0, 3])

# Sample weights
weights_0 = {'node_0': [2, 1],
             'node_1': [1, 2],
             'output': [1, 1]
            }


# Define predict_with_network()
def predict_with_network(input_data, weights):
    # Calculate node 0 value
    node_0_input = (input_data * weights['node_0']).sum()

    node_0_output = relu(node_0_input)

    # Calculate node 1 value
    node_1_input = (input_data * weights['node_1']).sum()
    node_1_output = relu(node_1_input)

    # Put node values into array: hidden_layer_outputs
    hidden_layer_outputs = np.array([node_0_output, node_1_output])

    # Calculate model output
    input_to_final_layer = (hidden_layer_outputs * weights['output']).sum()
    model_output = relu(input_to_final_layer)

    # Return model output
    return (model_output)

def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output

    output = max(0, input)

    # Return the value just calculated
    return (output)

# The actual target value, used to calculate the error
target_actual = 3

# Make prediction using original weights
model_output_0 = predict_with_network(input_data, weights_0)

# Calculate error: error_0
error_0 = model_output_0 - target_actual

print(error_0)
# Calculate the slope: slope
slope = 2 * input_data * error_0

# Print the slope
print(slope)

