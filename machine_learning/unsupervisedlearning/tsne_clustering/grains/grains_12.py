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
