# Import necessary modules

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
digits=datasets.load_digits()
# Create feature and target arrays
X = digits['data']
y = digits['target']
# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42, stratify=y,shuffle=True)

# Create a k-NN classifier with 7 neighbors: knn
knn = KNeighborsClassifier(n_neighbors=7)

# Fit the classifier to the training data
knn.fit(X_train,y_train)
# Print the accuracy
print("training data: ",knn.score(X_train, y_train))
print("testing data: ",knn.score(X_test, y_test))

'''A loop which checks because of which points the results are not 100 %'''
for i in range(0,360):
        if(knn.score(X_test[[i]], y_test[[i]])!=1):
            print(knn.score(X_test[[i]], y_test[[i]]))
            print(i)

#prints score of particular values
print(knn.score(X_test[[127]], y_test[[127]]))#checks the data with trained data'
print(X_test[127],y_test[127])#normally print the features and target values
# print(X.shape)
# print(y_test[[0]])
"""Train/Test Split + Fit/Predict/Accuracy
Now that you have learned about the importance of splitting your data into training and test sets, it's time to practice doing this on the digits dataset! After creating arrays for the features and target variable, you will split them into training and test sets, fit a k-NN classifier to the training data, and then compute its accuracy using the .score() method.

Instructions
100 XP
Instructions
100 XP
Import KNeighborsClassifier from sklearn.neighbors and train_test_split from sklearn.model_selection.
Create an array for the features using digits.data and an array for the target using digits.target.
Create stratified training and test sets using 0.2 for the size of the test set. Use a random state of 42. Stratify the split according to the labels so that they are distributed in the training and test sets as they are in the original dataset.
Create a k-NN classifier with 7 neighbors and fit it to the training data.
Compute and print the accuracy of the classifier's predictions using the .score() method."""