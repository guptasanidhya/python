from sklearn import datasets
from sklearn.linear_model import LinearRegression
from scipy.optimize import minimize
boston=datasets.load_boston()
X=boston.data
y=boston.target
# The squared error, summed over training examples
def my_loss(w):
    s = 0
    for i in range(y.size):
        # Get the true and predicted target values for example 'i'
        y_i_true = y[i]
        y_i_pred = w@X[i]
        s = s + (y_i_true - y_i_pred)**2
    return s

# Returns the w that makes my_loss(w) smallest
w_fit = minimize(my_loss, X[0]).x
print(w_fit)

# Compare with scikit-learn's LinearRegression coefficients
lr = LinearRegression(fit_intercept=False).fit(X,y)
print(lr.coef_)
"""
Minimizing a loss function
In this exercise you'll implement linear regression "from scratch" using scipy.optimize.minimize.

We'll train a model on the Boston housing price data set, which is already loaded into the variables X and y. For simplicity, we won't include an intercept in our regression model.

Instructions
0 XP
Fill in the loss function for least squares linear regression.
Print out the coefficients from fitting sklearn's LinearRegression.

Hint
The loss is the square of the difference between the true and predicted y-values (because we want them to be similar).
The access the coefficients, use lr.coef_.
"""