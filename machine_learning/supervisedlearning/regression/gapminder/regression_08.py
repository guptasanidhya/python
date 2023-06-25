# Import necessary modules
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import  GridSearchCV, train_test_split
df=pd.read_csv("gm_2008_region.csv")
X=df['fertility'].values.reshape(-1,1)
y=df['life'].values.reshape(-1,1)
# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.4)

# Create the hyperparameter grid
l1_space = np.linspace(0, 1, 30)
# alpha_space = np.logspace(-4, 0, 5)
# print(l1_space)
# param_grid = {    'alpha': alpha_space,
#     'l1_ratio': l1_space,
#     'fit_intercept': [True, False],
#     'max_iter': [100, 500, 1000]}
param_grid = {
    'l1_ratio': l1_space}
"""l1_ratio: This parameter determines the mix of L1 and L2 penalties. It is a value between 0 and 1, where 0 corresponds to Ridge regression (L2 penalty only) and 1 corresponds to Lasso regression (L1 penalty only)."""
# Instantiate the ElasticNet regressor: elastic_net
elastic_net = ElasticNet()

# Setup the GridSearchCV object: gm_cv
gm_cv = GridSearchCV(elastic_net, param_grid, cv=5)

# Fit it to the training data
gm_cv.fit(X_train,y_train)

# Predict on the test set and compute metrics
y_pred = gm_cv.predict(X_test)
r2 = gm_cv.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
print("Tuned ElasticNet l1 ratio: {}".format(gm_cv.best_params_))
print("Tuned ElasticNet R squared: {}".format(r2))
print("Tuned ElasticNet MSE: {}".format(mse))

"""Hold-out set in practice II: Regression
Remember lasso and ridge regression from the previous chapter? Lasso used the L1 penalty to regularize, while ridge used the L2 penalty. There is another type of regularized regression
 known as the elastic net. In elastic net regularization, the penalty term is a linear combination of 
 the L1 and L2 penalties:

a∗L1+b∗L2

In scikit-learn, this term is represented by the 'l1_ratio' parameter: An 'l1_ratio' of 1 corresponds to 
an L1 penalty, and anything lower is a combination of L1 and L2.

In this exercise, you will GridSearchCV to tune the 'l1_ratio' of an elastic net model trained on the 
Gapminder data. As in the previous exercise, use a hold-out set to evaluate your model's performance.

Instructions
0 XP
Instructions
0 XP
Import the following modules:
ElasticNet from sklearn.linear_model.
mean_squared_error from sklearn.metrics.
GridSearchCV and train_test_split from sklearn.model_selection.
Create training and test sets, with 40% of the data used for the test set. Use a random state of 42.
Specify the hyperparameter grid for 'l1_ratio' using l1_space as the grid of values to search over.
Instantiate the ElasticNet regressor.
Use GridSearchCV with 5-fold cross-validation to tune 'l1_ratio' on the training data X_train and y_train. This involves first instantiating the GridSearchCV object with the correct parameters and then fitting it to the training data.
Predict on the test set and compute the R2 and mean squared error."""