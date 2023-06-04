from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

samples=pd.read_csv('fish.csv')
samples.drop(columns = samples.columns[0], axis = 1, inplace= True)
print(samples)
scaler=StandardScaler()
kmeans=KMeans(n_clusters=4)
from sklearn.pipeline import make_pipeline
pipeline=make_pipeline(scaler,kmeans)
pipeline.fit(samples)
labels=pipeline.predict(samples)

species=[]
for label in labels:
    if label==0:
        species.append("Bream")
    elif label==1:
        species.append("Roach")
    elif label ==2:
        species.append("Smelt")
    elif label ==3:
        species.append("Pike")

# Import pandas
import pandas as pd

# Fit the pipeline to samples
pipeline.fit(samples)

# Calculate the cluster labels: labels
labels = pipeline.predict(samples)

# Create a DataFrame with labels and species as columns: df
df = pd.DataFrame({'labels':labels,'species':species})

# Create crosstab: ct
ct = pd.crosstab(df['labels'],df['species'])
# Display ct
print(ct)

"""
Scaling fish data for clustering
You are given an array samples giving measurements of fish. Each row represents an individual fish. The measurements, such as weight in grams, length in centimeters, and the percentage ratio of height to length, have very different scales. In order to cluster this data effectively, you'll need to standardize these features first. In this exercise, you'll build a pipeline to standardize and cluster the data.

These fish measurement data were sourced from the Journal of Statistics Education.

Instructions
100 XP
Import:
make_pipeline from sklearn.pipeline.
StandardScaler from sklearn.preprocessing.
KMeans from sklearn.cluster.
Create an instance of StandardScaler called scaler.
Create an instance of KMeans with 4 clusters called kmeans.
Create a pipeline called pipeline that chains scaler and kmeans. To do this, you just need to pass them in as arguments to make_pipeline().
"""

"""
Clustering the fish data
You'll now use your standardization and clustering pipeline from the previous exercise to cluster the fish by their measurements, and then create a cross-tabulation to compare the cluster labels with the fish species.

As before, samples is the 2D array of fish measurements. Your pipeline is available as pipeline, and the species of every fish sample is given by the list species.

Instructions
100 XP
Import pandas as pd.
Fit the pipeline to the fish measurements samples.
Obtain the cluster labels for samples by using the .predict() method of pipeline.
Using pd.DataFrame(), create a DataFrame df with two columns named 'labels' and 'species', using labels and species, respectively, for the column values.
Using pd.crosstab(), create a cross-tabulation ct of df['labels'] and df['species'].
"""