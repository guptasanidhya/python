# Import the necessary modules
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
import pandas as pd

df=pd.read_csv("diabetes.csv")
X=df.drop(['diabetes'],axis=1).values
print(X)
y=df["diabetes"].values
print(y)
names = df.drop(['diabetes'], axis=1).columns
# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4)

# Fit the regressor to the data
lasso.fit(X,y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(names)), lasso_coef)
plt.xticks(range(len(names)), names.values, rotation=60)
plt.margins(0.02)
plt.show()