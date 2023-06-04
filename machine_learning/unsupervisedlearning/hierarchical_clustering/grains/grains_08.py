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



# Calculate the linkage: mergings
mergings = linkage(samples,method='complete')
variety=["Kama","Rosa","Canadian"]
# Plot the dendrogram, using varieties as labels
dendrogram(mergings,
           labels=np.array(varieties),
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()


"""
Hierarchical clustering of the grain data
In the video, you learned that the SciPy linkage() function performs hierarchical clustering on an array of samples. Use the linkage() function to obtain a hierarchical clustering of the grain samples, and use dendrogram() to visualize the result. A sample of the grain measurements is provided in the array samples, while the variety of each grain sample is given by the list varieties.

Instructions
100 XP
Instructions
100 XP
Import:
linkage and dendrogram from scipy.cluster.hierarchy.
matplotlib.pyplot as plt.
Perform hierarchical clustering on samples using the linkage() function with the method='complete' keyword argument. Assign the result to mergings.
Plot a dendrogram using the dendrogram() function on mergings. Specify the keyword arguments labels=varieties, leaf_rotation=90, and leaf_font_size=6.
"""