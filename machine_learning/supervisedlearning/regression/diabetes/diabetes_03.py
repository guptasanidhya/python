# Import the necessary modules
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix,roc_curve
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv("diabetes.csv")
# print(df.groupby('diabetes').size())
X=df.iloc[:,df.columns!='diabetes']
y=df['diabetes']
# print(X,y)

#Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4,stratify=df['diabetes'],random_state=42)

# Create the classifier: logreg
logreg = LogisticRegression()

# Fit the classifier to the training data
logreg.fit(X_train,y_train)
# Predict the labels of the test set: y_pred
y_pred = logreg.predict(X_test)
print(X_test)
print(y_pred)
# Compute predicted probabilities: y_pred_prob
y_pred_prob = logreg.predict_proba(X_test)[:,1]
# z_pred_prob = logreg.predict_proba(X_test)
print(y_pred_prob)
# print(z_pred_prob)
# Generate ROC curve values: fpr, tpr, thresholds
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Plot ROC curve
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()