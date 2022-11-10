from tensorflow import keras
import tensorflow as tf
import pandas as pd
model=keras.Sequential()


# Define model 1 input layer shape
m1_inputs = tf.keras.Input(shape=(28*28,))
# For model 1, pass the input layer to layer 1 and layer 1 to layer 2
m1_layer1 = keras.layers.Dense(12, activation='sigmoid')(m1_inputs)
m1_layer2 = keras.layers.Dense(4, activation='softmax')(m1_layer1)

# Define model 2 input layer shape
m2_inputs = tf.keras.Input(shape=(10,))
# For model 2, pass the input layer to layer 1 and layer 1 to layer 2
m2_layer1 = keras.layers.Dense(12, activation='relu')(m2_inputs)
m2_layer2 = keras.layers.Dense(4, activation='softmax')(m2_layer1)

# Merge model outputs and define a functional model
merged = keras.layers.add([m1_layer2, m2_layer2])
model = keras.Model(inputs=[m1_inputs, m2_inputs], outputs=merged)

# Print a model summary
print(model.summary())

"""
Defining a multiple input model
In some cases, the sequential API will not be sufficiently flexible to accommodate your desired model architecture and you will need to use the functional API instead. If, for instance, you want to train two models with different architectures jointly, you will need to use the functional API to do this. In this exercise, we will see how to do this. We will also use the .summary() method to examine the joint model's architecture.

Note that keras has been imported from tensorflow for you. Additionally, the input layers of the first and second models have been defined as m1_inputs and m2_inputs, respectively. Note that the two models have the same architecture, but one of them uses a sigmoid activation in the first layer and the other uses a relu.
"""

"""
Nice work! Notice that the .summary() method yields a new column: connected to. This column tells you how layers connect to each other within the network. We can see that dense_2, for instance, is connected to the input_2 layer. We can also see that the add layer, which merged the two models, connected to both dense_1 and dense_3.
"""