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

# Create a k-NN classifier with 6 neighbors
knn =KNeighborsClassifier(n_neighbors=6)

#we have to use Imputer because KneighbourClassifier does not take nAN(missing) values
# knn=KNNImputer(n_neighbors=6)
# Fit the classifier to the data
knn.fit(X,y)


"""k-Nearest Neighbors: Fit
Having explored the Congressional voting records dataset, it is time now to build your first classifier. In this exercise, you will fit a k-Nearest Neighbors classifier to the voting dataset, which has once again been pre-loaded for you into a DataFrame df.

In the video, Hugo discussed the importance of ensuring your data adheres to the format required by the scikit-learn API. The features need to be in an array where each column is a feature and each row a different observation or data point - in this case, a Congressman's voting record. The target needs to be a single column with the same number of observations as the feature data. We have done this for you in this exercise. Notice we named the feature array X and response variable y: This is in accordance with the common scikit-learn practice.

Your job is to create an instance of a k-NN classifier with 6 neighbors (by specifying the n_neighbors parameter) and then fit it to the data. The data has been pre-loaded into a DataFrame called df.

Instructions
100 XP
Instructions
100 XP
Import KNeighborsClassifier from sklearn.neighbors.
Create arrays X and y for the features and the target variable. Here this has been done for you. Note the use of .drop() to drop the target variable 'party' from the feature array X as well as the use of the .values attribute to ensure X and y are NumPy arrays. Without using .values, X and y are a DataFrame and Series respectively; the scikit-learn API will accept them in this form also as long as they are of the right shape.
Instantiate a KNeighborsClassifier called knn with 6 neighbors by specifying the n_neighbors parameter.
Fit the classifier to the data using the .fit() method."""