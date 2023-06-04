
# Perform the necessary imports
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt
import pandas as pd


samples=pd.read_csv('../../clustering/fish/fish.csv')
samples.drop(columns = samples.columns[0], axis = 1, inplace= True)
species=samples.iloc[:,1]
print(species)
print(samples)
scaler=StandardScaler()
scaler.fit(samples)
StandardScaler(copy=True, with_mean=True, with_std=True)
scaled_samples = scaler.transform(samples)
# Create a PCA instance with 2 components: pca
pca = PCA(n_components=2)

# Fit the PCA instance to the scaled samples
pca.fit(scaled_samples)

# Transform the scaled samples: pca_features
pca_features = pca.transform(scaled_samples)
# Print the shape of pca_features
print(pca_features.shape)

xs=pca_features[:,0]
ys=pca_features[:,1]
plt.scatter(xs,ys,c=species)
plt.show()

"""
Dimension reduction of the fish measurements
In a previous exercise, you saw that 2 was a reasonable choice for the "intrinsic dimension" of the fish measurements. Now use PCA for dimensionality reduction of the fish measurements, retaining only the 2 most important components.

The fish measurements have already been scaled for you, and are available as scaled_samples.

Instructions
100 XP
Import PCA from sklearn.decomposition.
Create a PCA instance called pca with n_components=2.
Use the .fit() method of pca to fit it to the scaled fish measurements scaled_samples.
Use the .transform() method of pca to transform the scaled_samples. Assign the result to pca_features.
"""