import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df=pd.read_csv('seeds.csv')
# print(df.head())
x0=df.iloc[:,0]
x1=df.iloc[:,1]
x2=df.iloc[:,2]
x3=df.iloc[:,3]
x4=df.iloc[:,4]
x5=df.iloc[:,5]
x6=df.iloc[:,6]
x7=df.iloc[:,7]
samples=[x0,x1,x2,x3,x4,x5,x6]
# print(samples)
# Create a KMeans model with 3 clusters: model
model = KMeans(n_clusters=3)

# Use fit_predict to fit model and obtain cluster labels: labels
labels = model.fit_predict(df)
varieties=[]
for label in labels:
    if label==0:
        varieties.append("Kama")
    elif label==1:
        varieties.append("Rosa")
    elif label==2:
        varieties.append("Canadian")

# print(df.head())
# Create a DataFrame with labels and varieties as columns: df
df = pd.DataFrame({'labels': labels, 'varieties': varieties})
print(labels)
print(varieties)
# # Create crosstab: ct
ct = pd.crosstab(df['labels'],df['varieties'])
#
# # Display ct
print(ct)


"""
Evaluating the grain clustering
In the previous exercise, you observed from the inertia plot that 3 is a good number of clusters for the grain data. In fact, the grain samples come from a mix of 3 different grain varieties: "Kama", "Rosa" and "Canadian". In this exercise, cluster the grain samples into three clusters, and compare the clusters to the grain varieties using a cross-tabulation.

You have the array samples of grain samples, and a list varieties giving the grain variety for each sample. Pandas (pd) and KMeans have already been imported for you.

Instructions
100 XP
Instructions
100 XP
Create a KMeans model called model with 3 clusters.
Use the .fit_predict() method of model to fit it to samples and derive the cluster labels. Using .fit_predict() is the same as using .fit() followed by .predict().
Create a DataFrame df with two columns named 'labels' and 'varieties', using labels and varieties, respectively, for the column values. This has been done for you.
Use the pd.crosstab() function on df['labels'] and df['varieties'] to count the number of times each grain variety coincides with each cluster label. Assign the result to ct.
Hit submit to see the cross-tabulation!

"""