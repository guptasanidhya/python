# Import necessary modules
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

df=pd.read_csv("gm_2008_region.csv")
X=df['fertility'].values.reshape(-1,1)
y=df['life'].values.reshape(-1,1)
# Create a linear regression object: reg
reg = LinearRegression()
# Perform 3-fold CV
cvscores_3 = cross_val_score(reg,X,y,cv=3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 =cross_val_score(reg,X,y,cv=10)
print(np.mean(cvscores_10))
