from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
"""
StandardScaler and KMeans have similar methods
Use fit() / transform() with StandardScaler
Use fit() / predict() with KMeans

"""
samples=pd.read_csv('wine.csv')
samples.drop('class_name', axis=1,inplace=True)
scaler = StandardScaler()
# print(samples)
scaler.fit(samples)
StandardScaler(copy=True, with_mean=True, with_std=True)
samples_scaled = scaler.transform(samples)
print(samples_scaled)

model=KMeans(n_clusters=3)
labels=model.fit_predict(samples)
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