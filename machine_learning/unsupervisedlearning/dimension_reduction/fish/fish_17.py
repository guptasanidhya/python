
# Perform the necessary imports
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

samples=pd.read_csv('fish.csv')
samples.drop(columns = samples.columns[0], axis = 1, inplace= True)
print(samples)
scaler=StandardScaler()
scaler.fit(samples)
StandardScaler(copy=True, with_mean=True, with_std=True)
scaled_samples = scaler.transform(samples)
pca=PCA()
pca.fit(scaled_samples)
# Plot the explained variances
features = range(pca.n_components_)
print(features)
print(pca.explained_variance_)
plt.bar(features, pca.explained_variance_)
plt.xlabel('PCA feature')
plt.ylabel('variance')
plt.xticks(features)
plt.show()