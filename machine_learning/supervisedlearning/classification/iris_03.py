import pandas as pd
import numpy as np
from sklearn.neighbors  import KNeighborsClassifier
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
feature=['Species','Id']
df =pd.read_csv('Iris.csv')
df.replace(('Iris-setosa','Iris-versicolor','Iris-virginica'),(0,1,2),inplace=True)
# print(df.head())
X=df.drop(feature,axis=1).values
y=df['Species'].values

steps = [('imputation', SimpleImputer(missing_values=np.nan, strategy='most_frequent',verbose=0)),
        ('logreg', LogisticRegression())]
# Setup the pipeline with the required steps: steps
pipeline = Pipeline(steps)

pipeline.fit(X,y)
print(pipeline.predict([[6.3,2.5,4.9,1.5]]))
