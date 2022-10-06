import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
samples=pd.read_csv('lcd-digits.csv')
# Select the 0th row: digit
digit = samples.iloc[0,:]

# Print digit

npp=np.array(digit)
bitmap=npp.reshape((13,8))
# Print bitmap
print(bitmap)

# Use plt.imshow to display bitmap
plt.imshow(bitmap, cmap='gray', interpolation='nearest')
plt.colorbar()
plt.show()
