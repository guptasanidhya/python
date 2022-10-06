from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pickle
df=pd.read_csv("diabetes.csv")
"""
1.pregnancies,glucose(Plasma glucose concentration a 2 hours in an oral glucose tolerance test)
,diastolic(Diastolic blood pressure (mm Hg))
,triceps(Triceps skin fold thickness (mm)),insulin(2-Hour serum insulin (mu U/ml))
,bmi(Body mass index (weight in kg/(height in m)^2))
,dpf(Diabetes pedigree function),age
"""
# print(df.groupby('diabetes').size())
X=df.iloc[:,df.columns!='diabetes']
y=df['diabetes']
steps = [('imputation', SimpleImputer(missing_values=np.nan, strategy='most_frequent',verbose=0)),
        ('SVC()', LogisticRegression(solver='liblinear'))]
# Setup the pipeline with the required steps: steps
pipeline = Pipeline(steps)

pipeline.fit(X,y)
pickle.dump(pipeline, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(pipeline.predict([[7,107,74,0,0,29.6,0.254,31]]))
print(pipeline.predict_proba([[7,107,74,0,0,29.6,0.254,31]]))