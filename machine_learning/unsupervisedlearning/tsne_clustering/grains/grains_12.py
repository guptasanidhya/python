# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
samples=pd.read_csv('seeds.csv')
model = KMeans(n_clusters=3)
labels=model.fit_predict(samples)
varieties=[]
for label in labels:
    if label==0:
        varieties.append("Kama")
    elif label==1:
        varieties.append("Rosa")
    elif label ==2:
        varieties.append("Canadian")

# Import TSNE
from sklearn.manifold import TSNE

# Create a TSNE instance: model
model = TSNE(learning_rate=200)

# Apply fit_transform to samples: tsne_features
tsne_features =model.fit_transform(samples)

# Select the 0th feature: xs
xs = tsne_features[:,0]

# Select the 1st feature: ys
ys = tsne_features[:,1]

# Scatter plot, coloring by variety_numbers
plt.scatter(xs,ys,c=labels)
plt.show()

"""
t-SNE visualization of grain dataset
In the video, you saw t-SNE applied to the iris dataset. In this exercise, you'll apply t-SNE to the grain samples data and inspect the resulting t-SNE features using a scatter plot. You are given an array samples of grain samples and a list variety_numbers giving the variety number of each grain sample.

Instructions
100 XP
Import TSNE from sklearn.manifold.
Create a TSNE instance called model with learning_rate=200.
Apply the .fit_transform() method of model to samples. Assign the result to tsne_features.
Select the column 0 of tsne_features. Assign the result to xs.
Select the column 1 of tsne_features. Assign the result to ys.
Make a scatter plot of the t-SNE features xs and ys. To color the points by the grain variety, specify the additional keyword argument c=variety_numbers.
"""