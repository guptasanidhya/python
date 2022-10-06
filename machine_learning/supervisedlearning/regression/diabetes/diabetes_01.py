# Import necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
import pandas as pd

df=pd.read_csv("diabetes.csv")
# print(df.groupby('diabetes').size())
X=df.iloc[:,df.columns!='diabetes']
y=df['diabetes']
# print(X,y)

#Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,stratify=df['diabetes'],random_state=42)

# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors=6)
# Fit the classifier to the training data
knn.fit(X_train,y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test,y_pred ))
