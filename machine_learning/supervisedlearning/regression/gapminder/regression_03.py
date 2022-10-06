# Import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("gm_2008_region.csv")
# Create the regressor: reg
reg = LinearRegression()
y=df['life'].values
X_fertility=df['fertility'].values
y_reshaped = y.reshape(-1,1)
X_reshaped = X_fertility.reshape(-1,1)
# print(min(X_reshaped))
# print(max(X_reshaped))
# print(X_fertility)
# print(X_reshaped)
# print(y)

# Create the prediction space
prediction_space = np.linspace(min(X_reshaped), max(X_reshaped))
print("prediction_space:",prediction_space)
# Fit the model to the data
reg.fit(X_reshaped,y_reshaped )

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)
# print(y_pred)
# Print R^2
print(reg.score(X_reshaped , y_reshaped ))

# Plot regression line
plt.plot(prediction_space, y_pred, color='black', linewidth=3)

plt.scatter(X_reshaped,y_reshaped)
# plt.scatter(2.73,75.3,color="red")
# plt.scatter(1.28,77.26,color="blue")
plt.xlabel("prediction_space(fertility)")
plt.ylabel("y_pred(life)")
plt.show()
