import numpy as np
import pandas as pd
import keras
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import to_categorical

df=pd.read_csv('titanic_all_numeric.csv')
# print(df.describe())
x = np.asarray(df.survived).astype('float32')
df['age_was_missing']=df['age_was_missing'].astype('float32')
print(df.age_was_missing)
predictors = df.drop(['survived'], axis=1)
# print(predictors)
target = to_categorical(x)

n_cols = predictors.shape[1]
# Set up the model
model = Sequential()

# Add the first layer
model.add(Dense(32, activation='relu', input_shape=(n_cols,)))

# Add the output layer
model.add(Dense(2, activation='softmax'))

# Compile the model
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
print(predictors)
# Fit the model
model.fit(predictors, target)

# Calculate predictions: predictions
predictions = model.predict([[2.      ,  34.      ,   0.      ,   0.      ,  13.      ,
          1.      ,   0.     ,   0.      ,   0.      ,   1.    ]])

# Calculate predicted probability of survival: predicted_prob_true
predicted_prob_true = predictions[:,1]

# print predicted_prob_true
print(predicted_prob_true)
model.save('model_file.h5')

"""
Last steps in classification models
You'll now create a classification model using the titanic dataset, which has been pre-loaded into a DataFrame called df. You'll take information about the passengers and predict which ones survived.

The predictive variables are stored in a NumPy array predictors. The target to predict is in df.survived, though you'll have to manipulate it for Keras. The number of predictive features is stored in n_cols.

Here, you'll use the 'sgd' optimizer, which stands for Stochastic Gradient Descent. You'll learn more about this in the next chapter!

Instructions
0 XP
Instructions
0 XP
Convert df.survived to a categorical variable using the to_categorical() function.
Specify a Sequential model called model.
Add a Dense layer with 32 nodes. Use 'relu' as the activation and (n_cols,) as the input_shape.
Add the Dense output layer. Because there are two outcomes, it should have 2 units, and because it is a classification model, the activation should be 'softmax'.
Compile the model, using 'sgd' as the optimizer, 'categorical_crossentropy' as the loss function, and metrics=['accuracy'] to see the accuracy (what fraction of predictions were correct) at the end of each epoch.
Fit the model using the predictors and the target.

Hint
Use the to_categorical() on df.survived to create the target.
Assign Sequential() to model to begin specifying the model.
Use the .add() method of model to add Dense layers with the appropriate number of units. Use the activation parameter to specify 'relu' as the activation function for the input layer and 'softmax' as the activation function for the output layer. Be sure to specify input_shape=(n_cols,) for the first layer.
To compile your model, use model.compile() and specify the arguments mentioned in the instructions for the optimizer, loss, and metrics parameters.
To fit the model, use model.fit() with predictors as the first argument and target as the second argument.
"""

"""
Making predictions
The trained network from your previous coding exercise is now stored as model. New data to make predictions is stored in a NumPy array as pred_data. Use model to make predictions on your new data.

In this exercise, your predictions will be probabilities, which is the most common way for data scientists to communicate their predictions to colleagues.

Instructions
100 XP
Create your predictions using the model's .predict() method on pred_data.
Use NumPy indexing to find the column corresponding to predicted probabilities of survival being True. This is the second column (index 1) of predictions. Store the result in predicted_prob_true and print it.
"""
"""
prediction data or test data
array([[  2.      ,  34.      ,   0.      ,   0.      ,  13.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  31.      ,   1.      ,   1.      ,  26.25    ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  11.      ,   1.      ,   2.      , 120.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,   0.42    ,   0.      ,   1.      ,   8.5167  ,
          1.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  27.      ,   0.      ,   0.      ,   6.975   ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  31.      ,   0.      ,   0.      ,   7.775   ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  39.      ,   0.      ,   0.      ,   0.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  18.      ,   0.      ,   0.      ,   7.775   ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  39.      ,   0.      ,   0.      ,  13.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  33.      ,   1.      ,   0.      ,  53.1     ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  26.      ,   0.      ,   0.      ,   7.8875  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  39.      ,   0.      ,   0.      ,  24.15    ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  35.      ,   0.      ,   0.      ,  10.5     ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,   6.      ,   4.      ,   2.      ,  31.275   ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  30.5     ,   0.      ,   0.      ,   8.05    ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  29.699118,   0.      ,   0.      ,   0.      ,
          1.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  23.      ,   0.      ,   0.      ,   7.925   ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  31.      ,   1.      ,   1.      ,  37.0042  ,
          1.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  43.      ,   0.      ,   0.      ,   6.45    ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  10.      ,   3.      ,   2.      ,  27.9     ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  52.      ,   1.      ,   1.      ,  93.5     ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  27.      ,   0.      ,   0.      ,   8.6625  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  38.      ,   0.      ,   0.      ,   0.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  27.      ,   0.      ,   1.      ,  12.475   ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,   2.      ,   4.      ,   1.      ,  39.6875  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,   6.95    ,
          1.      ,   1.      ,   0.      ,   1.      ,   0.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,  56.4958  ,
          1.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,   1.      ,   0.      ,   2.      ,  37.0042  ,
          1.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,   7.75    ,
          1.      ,   1.      ,   0.      ,   1.      ,   0.      ],
       [  1.      ,  62.      ,   0.      ,   0.      ,  80.      ,
          0.      ,   0.      ,   0.      ,   0.      ,   0.      ],
       [  3.      ,  15.      ,   1.      ,   0.      ,  14.4542  ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  2.      ,   0.83    ,   1.      ,   1.      ,  18.75    ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,   7.2292  ,
          1.      ,   1.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  23.      ,   0.      ,   0.      ,   7.8542  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  18.      ,   0.      ,   0.      ,   8.3     ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  39.      ,   1.      ,   1.      ,  83.1583  ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  21.      ,   0.      ,   0.      ,   8.6625  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,   8.05    ,
          1.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  32.      ,   0.      ,   0.      ,  56.4958  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  29.699118,   0.      ,   0.      ,  29.7     ,
          1.      ,   1.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  20.      ,   0.      ,   0.      ,   7.925   ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  16.      ,   0.      ,   0.      ,  10.5     ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  30.      ,   0.      ,   0.      ,  31.      ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  34.5     ,   0.      ,   0.      ,   6.4375  ,
          1.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  17.      ,   0.      ,   0.      ,   8.6625  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  42.      ,   0.      ,   0.      ,   7.55    ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   8.      ,   2.      ,  69.55    ,
          1.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  35.      ,   0.      ,   0.      ,   7.8958  ,
          1.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  2.      ,  28.      ,   0.      ,   1.      ,  33.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  29.699118,   1.      ,   0.      ,  89.1042  ,
          0.      ,   1.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,   4.      ,   4.      ,   2.      ,  31.275   ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  74.      ,   0.      ,   0.      ,   7.775   ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,   9.      ,   1.      ,   1.      ,  15.2458  ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  1.      ,  16.      ,   0.      ,   1.      ,  39.4     ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  44.      ,   1.      ,   0.      ,  26.      ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  18.      ,   0.      ,   1.      ,   9.35    ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  45.      ,   1.      ,   1.      , 164.8667  ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  51.      ,   0.      ,   0.      ,  26.55    ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  24.      ,   0.      ,   3.      ,  19.2583  ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,   7.2292  ,
          1.      ,   1.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  41.      ,   2.      ,   0.      ,  14.1083  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  21.      ,   1.      ,   0.      ,  11.5     ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  48.      ,   0.      ,   0.      ,  25.9292  ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   8.      ,   2.      ,  69.55    ,
          0.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  24.      ,   0.      ,   0.      ,  13.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  42.      ,   0.      ,   0.      ,  13.      ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  27.      ,   1.      ,   0.      ,  13.8583  ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  1.      ,  31.      ,   0.      ,   0.      ,  50.4958  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,   9.5     ,
          1.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,   4.      ,   1.      ,   1.      ,  11.1333  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  26.      ,   0.      ,   0.      ,   7.8958  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  47.      ,   1.      ,   1.      ,  52.5542  ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  33.      ,   0.      ,   0.      ,   5.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  47.      ,   0.      ,   0.      ,   9.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  28.      ,   1.      ,   0.      ,  24.      ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  15.      ,   0.      ,   0.      ,   7.225   ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  20.      ,   0.      ,   0.      ,   9.8458  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  19.      ,   0.      ,   0.      ,   7.8958  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   0.      ,   0.      ,   7.8958  ,
          1.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  56.      ,   0.      ,   1.      ,  83.1583  ,
          0.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  2.      ,  25.      ,   0.      ,   1.      ,  26.      ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  33.      ,   0.      ,   0.      ,   7.8958  ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  22.      ,   0.      ,   0.      ,  10.5167  ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  2.      ,  28.      ,   0.      ,   0.      ,  10.5     ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  25.      ,   0.      ,   0.      ,   7.05    ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  39.      ,   0.      ,   5.      ,  29.125   ,
          0.      ,   0.      ,   0.      ,   1.      ,   0.      ],
       [  2.      ,  27.      ,   0.      ,   0.      ,  13.      ,
          1.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  19.      ,   0.      ,   0.      ,  30.      ,
          0.      ,   0.      ,   0.      ,   0.      ,   1.      ],
       [  3.      ,  29.699118,   1.      ,   2.      ,  23.45    ,
          0.      ,   1.      ,   0.      ,   0.      ,   1.      ],
       [  1.      ,  26.      ,   0.      ,   0.      ,  30.      ,
          1.      ,   0.      ,   1.      ,   0.      ,   0.      ],
       [  3.      ,  32.      ,   0.      ,   0.      ,   7.75    ,
          1.      ,   0.      ,   0.      ,   1.      ,   0.      ]],
      dtype=float32)
"""