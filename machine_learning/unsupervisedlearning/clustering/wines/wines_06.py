from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

samples=pd.read_csv('wine.csv')
samples.drop('class_name', axis=1,inplace=True)
print(samples)
scaler=StandardScaler()
kmeans=KMeans(n_clusters=3)
from sklearn.pipeline import make_pipeline
pipeline=make_pipeline(scaler,kmeans)
pipeline.fit(samples)
labels=pipeline.predict(samples)

varieties=[]
for label in labels:
    if label==0:
        varieties.append("Barolo")
    elif label==1:
        varieties.append("Grignolino")
    elif label ==2:
        varieties.append("Barbera")

# print(df.head())
# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})
print(labels)
print(varieties)
# Create crosstab: ct
ct = pd.crosstab(df['labels'],df['varieties'])
#
# # Display ct
print(ct)