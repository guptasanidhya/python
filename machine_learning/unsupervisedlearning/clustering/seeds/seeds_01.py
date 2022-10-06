import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df=pd.read_csv('seeds.csv')
"""("Area", "Perimeter", "Compactness", "Length", "Width", "Asymetry.coef", "Grove.length", "Type")"""
# print(df.head())
# x0=df.iloc[:,0]
# x1=df.iloc[:,1]
# x2=df.iloc[:,2]
# x3=df.iloc[:,3]
# x4=df.iloc[:,4]
# x5=df.iloc[:,5]
# x6=df.iloc[:,6]
# x7=df.iloc[:,7]
# samples=[x0,x1,x2,x3,x4,x5,x6,x7]

ks = range(1, 6)

inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(k)

    # Fit model to samples
    model.fit(df)

    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)

ks = range(1, 6)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model=KMeans(n_clusters=k)

    # Fit model to samples
    model.fit(df)

    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)

# Plot ks vs inertias
plt.plot(ks, inertias, '-o')
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()

"""
How many clusters of grain?
In the video, you learned how to choose a good number of clusters for a dataset using the k-means inertia graph. You are given an array samples containing the measurements (such as area, perimeter, length, and several others) of samples of grain. What's a good number of clusters in this case?

KMeans and PyPlot (plt) have already been imported for you.

This dataset was sourced from the UCI Machine Learning Repository.

Instructions
70 XP
Instructions
70 XP
For each of the given values of k, perform the following steps:
Create a KMeans instance called model with k clusters.
Fit the model to the grain data samples.
Append the value of the inertia_ attribute of model to the list inertias.
The code to plot ks vs inertias has been written for you, so hit submit to see the plot!
"""