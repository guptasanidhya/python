from tensorflow import keras,Variable,random,ones,matmul
import tensorflow as tf
from sklearn.metrics import confusion_matrix
# Define the layer 1 weights
w1 = Variable(random.normal([23,7]))

# Initialize the layer 1 bias
b1 = Variable(ones([7]))

# Define the layer 2 weights
w2 = Variable(random.normal([7,1]))

# Define the layer 2 bias
b2 = Variable([0])

import pandas as pd

df =pd.read_csv('uci_credit_card.csv')
# print(df.columns)
default= df['default.payment.next.month'].values
new_df = df.drop(['default.payment.next.month','ID'], axis=1).values
borrower_features=Variable(new_df,tf.float32)

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
opt = keras.optimizers.RMSprop(learning_rate=0.01, momentum=0.99)

test_features=borrower_features[:100]
test_targets=default[:100]
# Train the model
for j in range(100):
    # Complete the optimizer
	opt.minimize(lambda: loss_function(w1, b1, w2, b2),
                 var_list=[w1, b1, w2, b2])

# Make predictions with model using test features
model_predictions = model(w1, b1, w2, b2, test_features)

# Construct the confusion matrix
confusion_matrix(test_targets, model_predictions)