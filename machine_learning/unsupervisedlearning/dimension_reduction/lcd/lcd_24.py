import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
samples=pd.read_csv('lcd-digits.csv')
# Select the 0th row: digit
digit = samples.iloc[0,:]
def show_as_image(sample):
    # print(sample)
    bitmap = sample.reshape((13, 8))
    print("##########################################################################################")
    # print(bitmap)
    plt.figure()
    plt.imshow(bitmap, cmap='gray', interpolation='nearest')
    plt.colorbar()
    plt.show()

# Import NMF
from sklearn.decomposition import NMF

# Create an NMF model: model
model = NMF(n_components=7)

# Apply fit_transform to samples: features
features = model.fit_transform(samples)
# print(model.components_)
# Call show_as_image on each component
for component in model.components_:
    show_as_image(component)

# Select the 0th row of features: digit_features
digit_features = features[0,:]

# Print digit_features
print(digit_features)

"""Now use what you've learned about NMF to decompose the digits dataset. You are again given the 
digit images as a 2D array samples. This time, you are also provided with a function show_as_image()
 that displays the image encoded by any 1D array:"""
"""
After you are done, take a moment to look through the plots and notice how NMF has expressed the digit as a sum of the components!
"""