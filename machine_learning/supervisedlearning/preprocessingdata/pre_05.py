from sklearn.neighbors  import KNeighborsClassifier
from sklearn.impute import KNNImputer
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
columnnames=['party','handicapped-infants','water-project-cost-sharing','adoption-of-the-budget-resolution',
                       'physician-fee-freeze',' el-salvador-aid','religious-groups-in-schools','satellite',
                       'aid-to-nicaraguan-contras',' missile','immigration','synfuels-corporation-cutback',
                       'education-spending','superfund-right-to-sue','crime','duty-free-exportsduty-free-exports',
                       'export-administration-act-south-africa']
df=pd.read_csv("house-votes-8.csv", names=columnnames)
df[df == '?'] = np.NAN
# Setup the Imputation transformer: imp
imp = SimpleImputer(missing_values='NaN', strategy='most_frequent')
print(imp)
# Instantiate the SVC classifier: clf
clf = SVC()

# Setup the pipeline with the required steps: steps
steps = [('imputation', imp),
        ('SVM', clf)]

"""Imputing missing data in a ML Pipeline I
As you've come to appreciate, there are many steps to building a model, from creating training and test sets, to fitting a classifier or regressor, to tuning its parameters, to evaluating its performance on new data.
 Imputation can be seen as the first step of this machine learning process,
  the entirety of which can be viewed within the context of a pipeline.
   Scikit-learn provides a pipeline constructor that allows you to piece together these steps
    into one process and thereby simplify your workflow.

You'll now practice setting up a pipeline with two steps: the imputation step, followed by the
 instantiation of a classifier. You've seen three classifiers in this course so far: k-NN,
  logistic regression, and the decision tree. You will now be introduced to a fourth one -
   the Support Vector Machine, or SVM. For now, do not worry about how it works under the hood.
    It works exactly as you would expect of the scikit-learn estimators that you have worked with
     previously, in that it has the same .fit() and .predict() methods as before.

"""