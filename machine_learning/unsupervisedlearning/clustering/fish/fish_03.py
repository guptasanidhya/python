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
