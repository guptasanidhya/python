from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
df=datasets.load_digits()

x=df.data
y=df.target
z=df.feature_names
print(z)
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
# Fit one-vs-rest logistic regression classifier
lr_ovr = LogisticRegression(multi_class='ovr')
lr_ovr.fit(X_train, y_train)

print("OVR training accuracy:", lr_ovr.score(X_train, y_train))
print("OVR test accuracy    :", lr_ovr.score(X_test, y_test))

# Fit softmax classifier
lr_mn = LogisticRegression(multi_class='multinomial')
lr_mn.fit(X_train, y_train)

print("Softmax training accuracy:", lr_mn.score(X_train, y_train))
print("Softmax test accuracy    :", lr_mn.score(X_test, y_test))
"""
One vs. all and multinomial ask different questions.

OVA asks - if I compare the subjects who responded XXXX to all others, what can I say?

Multinomial asks - What can be said about the differences among the people who respond at each level?

Let me make this concrete. Suppose your DV is "Who did you vote for in 2012 for President?" with choices being "Obama", "Romney", "Stein", "Johnson", "Other" and "Did not vote". Your IVs are sex, age, race, etc. And you have a really big and random sample (good luck!)

Now, you can do OVA with (say) "Obama" vs. all others. That compares Obama voters to everyone else - all the others are lumped together. You would find things like "Black voters are more likely to vote for Obama than anyone else".

But there could be (and probably are) differences between Romney voters, Stein voters and people who stayed home. You can look at those with multinomial.
"""

