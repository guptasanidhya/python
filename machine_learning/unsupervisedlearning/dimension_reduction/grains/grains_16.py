
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
samples=pd.read_csv('seeds-width-vs-length.csv')
# Perform the necessary imports
from scipy.stats import pearsonr

# Import PCA
from sklearn.decomposition import PCA

# Make a scatter plot of the untransformed points
plt.scatter(samples.iloc[:,0], samples.iloc[:,1])

# Create PCA instance: model
model = PCA()
# Fit model to points
model.fit(samples)

# Get the mean of the grain samples: mean
mean = model.mean_

print(mean[0],mean[1])
print(model.components_)
# Get the first principal component: first_pc
first_pc = model.components_[0,:]
print(first_pc[0],first_pc[1])
# Plot first_pc as an arrow, starting at mean
plt.arrow(mean[0], mean[1], first_pc[0], first_pc[1], color='red', width=0.01)#single principle component
"""Syntax: matplotlib.pyplot.arrow(x, y, dx, dy, **kwargs)
Parameters: 
x, y: The x and y coordinates of the arrow base. 
dx, dy: The length of the arrow along x and y direction. """
#Keep axes on same scale
plt.axis('equal')
plt.show()
"""
"Principal components"= directions of variance
PCA aligns principal components with the axes
Available as components_ attribute of PCA object
Each row defines displacement from mean
"""

"""
The first principal component
The first principal component of the data is the direction
 in which the data varies the most. In this exercise, your job is to use PCA to find the first principal
 component of the length and width measurements of the grain samples, and represent it as an arrow on the scatter plot.
The array grains gives the length and width of the grain samples. PyPlot (plt) and PCA have already been imported for you.
"""