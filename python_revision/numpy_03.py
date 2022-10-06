# baseball is available as a regular list of lists
# updated is available as 2D numpy array
baseball=[]
updated=[]
# Import numpy package
import numpy as np

# Create np_baseball (3 cols)
np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball+updated)

# Create numpy array: conversion
ls=[0.0254,0.453592,1]
conversion=np.array(ls)
# Print out product of np_baseball and conversion
print(np_baseball*conversion)