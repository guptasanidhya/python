# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
samples=pd.read_csv('seeds-width-vs-length.csv')
# Perform the necessary imports
from scipy.stats import pearsonr

# Assign the 0th column of grains: width
width = samples.iloc[:,0]

# Assign the 1st column of grains: length
length = samples.iloc[:,1]

# Scatter plot width vs length
plt.scatter(width,length)
plt.axis('equal')
plt.show()

# Calculate the Pearson correlation
correlation, pvalue = pearsonr(width,length)

# Display the correlation
print(correlation)

"""
Recall that the principal components are the directions along which the the data varies."""
"""The Pearson correlation coefficient (named for Karl Pearson) can be used to summarize the 
strength of the linear relationship between two data samples. The Pearson's correlation coefficient
 is calculated as the covariance of the two variables divided by the product of the standard deviation 
 of each data sample."""

"""
Correlated data in nature
You are given an array grains giving the width and length of samples of grain. You suspect that width and length will be correlated. To confirm this, make a scatter plot of width vs length and measure their Pearson correlation.

Instructions
100 XP
Import:
matplotlib.pyplot as plt.
pearsonr from scipy.stats.
Assign column 0 of grains to width and column 1 of grains to length.
Make a scatter plot with width on the x-axis and length on the y-axis.
Use the pearsonr() function to calculate the Pearson correlation of width and length.
"""