from sklearn.metrics import mean_squared_error
import numpy as np
input_data=[np.array([0,3]),np.array([1,3])]
# Sample weights
weights_0 = {'node_0': [2, 1],
             'node_1': [1, 2],
             'output': [1, 1]
            }
weights_1 = {'node_0': [2, 1],
             'node_1': [1, 1],
             'output': [1, 0]
            }
target_actuals=[3,9]
# Create model_output_0
model_output_0 = []
# Create model_output_1
model_output_1 = []

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


# Loop over input_data
for row in input_data:
    # Append prediction to model_output_0
    model_output_0.append(predict_with_network(row, weights_0))

    # Append prediction to model_output_1
    model_output_1.append(predict_with_network(row, weights_1))

# Calculate the mean squared error for model_output_0: mse_0
mse_0 = mean_squared_error(target_actuals, model_output_0)

# Calculate the mean squared error for model_output_1: mse_1
mse_1 = mean_squared_error(target_actuals, model_output_1)

# Print mse_0 and mse_1
print("Mean squared error with weights_0: %f" % mse_0)
print("Mean squared error with weights_1: %f" % mse_1)