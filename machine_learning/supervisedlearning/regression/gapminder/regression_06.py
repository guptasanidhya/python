# Import Lasso
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import Lasso

df=pd.read_csv("gm_2008_region.csv")
X=df.drop(['fertility','Region'],axis=1).values
print(X)
y=df["fertility"].values
print(y)
names = df.drop(['fertility','Region'], axis=1).columns
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
