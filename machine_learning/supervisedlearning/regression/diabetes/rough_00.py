import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.neighbors import KNeighborsClassifier
df=pd.read_csv("diabetes.csv")
# print(df.groupby('diabetes').size())
X=df.iloc[:,df.columns!='diabetes']
y=df['diabetes']
# print(df.describe)
""" stratify=df['diabetes'] ensures that the splitting is done while preserving the proportion of the 'diabetes' classes in both the training and testing datasets."""
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,stratify=df['diabetes'],random_state=42)

c_space=np.logspace(-5,8,15)
param_grid={'C':c_space}
logreg=LogisticRegression(solver='liblinear')
logreg_cv=GridSearchCV(logreg,param_grid,cv=5)
logreg_cv.fit(X,y)
print(logreg_cv.best_params_)
print(logreg_cv.best_score_)