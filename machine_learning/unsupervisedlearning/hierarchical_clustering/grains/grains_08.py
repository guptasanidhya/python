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
