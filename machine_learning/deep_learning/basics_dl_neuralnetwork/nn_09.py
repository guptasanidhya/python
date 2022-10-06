
import numpy as np
# The data point you will make a prediction for
input_data = np.array([0, 3])
n_updates = 20
mse_hist = []
# Sample weights
weights_0 = {'node_0': [2, 1],
             'node_1': [1, 2],
             'output': [1, 1]
            }

# Set the learning rate: learning_rate
learning_rate = 0.01
target=3
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
error_corrected=False
while error_corrected==False:
# Make prediction using original weights
    model_output_0 = predict_with_network(input_data, weights_0)

    # Calculate error: error_0
    error_0 = model_output_0 - target_actual

    print(error_0)
    # Calculate the slope: slope
    slope = 2 * input_data * error_0

    weights_0['node_0']=weights_0['node_0']-learning_rate*slope[0]
    weights_0['node_1']=weights_0['node_1']-learning_rate*slope[1]
    # Update the weights: weights_updated

    # weights_updated = weights_0-learning_rate*slope

    # Get updated predictions: preds_updated
    preds_updated = predict_with_network(input_data, weights_0)
    # Calculate updated error: error_updated
    error_updated = preds_updated-target

    # Print the updated error
    print(error_updated)
    if error_updated==0:
        error_corrected=True
    else:
        error_corrected=False