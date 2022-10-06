# Import the necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import scale

"""['pregnancies', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi',
       'dpf', 'age', 'diabetes']"""
df=pd.read_csv("diabetes.csv")
X=df.loc[:,df.columns!='diabetes']
X_scaled = scale(X)
# X=df.loc[:,['glucose','age','bmi']]
y=df['diabetes']
# print(X)
# Create the hyperparameter grid

c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space,'penalty': ['l1', 'l2']}

# Instantiate the logistic regression classifier: logreg
logreg = LogisticRegression(solver='liblinear')

# Create train and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,stratify=y,random_state=42)

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg,param_grid,cv=5)
# Fit it to the training data
logreg_cv.fit(X_train,y_train)
y_pred=logreg_cv.predict(X_test)


X=df.drop('diabetes', axis=1).values
yy = df['diabetes'].values
# print(X_test)
print(yy[83])
print(X[83])
# create a Boolean index for the wrong classifications
classification_is_wrong = y_test[83] != y_pred[83]
print(classification_is_wrong,y_test[83],y_pred[83])
classification_is_wrong = y_test != y_pred

# print the file names of the wrongly classified mails
print(classification_is_wrong)
print(logreg_cv.predict([[0,101,65,28,0,24.6,0.237,22]]))

