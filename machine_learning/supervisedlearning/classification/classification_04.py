# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np
columnnames=['party','handicapped-infants','water-project-cost-sharing','adoption-of-the-budget-resolution',
                       'physician-fee-freeze',' el-salvador-aid','religious-groups-in-schools','satellite',
                       'aid-to-nicaraguan-contras',' missile','immigration','synfuels-corporation-cutback',
                       'education-spending','superfund-right-to-sue','crime','duty-free-exportsduty-free-exports',
                       'export-administration-act-south-africa']
df=pd.read_csv("house-votes-8.csv", names=columnnames)
df.replace(('y','n','?'),(1,0,np.NAN),inplace=True)
df.fillna(method='bfill',inplace=True)
df.fillna(method='ffill',inplace=True)
# Create arrays for the features and the response variable
y = df['party'].values
X = df.drop('party', axis=1).values

# Create a k-NN classifier with 6 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=6)
# knn=KNNImputer(n_neighbors=6)
# Fit the classifier to the data
knn.fit(X,y)

# Predict the labels for the training data X
y_pred =knn.predict(X)

# Predict and print the label for the new data point X_new
new_prediction =knn.predict(X)
print("Prediction: {}".format(new_prediction))
