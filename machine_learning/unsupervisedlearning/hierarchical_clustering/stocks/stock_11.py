import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
movements=pd.read_csv('company-stock.csv')
companies=np.array(movements.iloc[:,0])
print(movements)
movements.drop(columns = movements.columns[0], axis = 1, inplace= True)
# Import normalize
from sklearn.preprocessing import normalize

# Normalize the movements: normalized_movements
normalized_movements = normalize(movements)

# Calculate the linkage: mergings
mergings = linkage(normalized_movements,method='complete')

# Plot the dendrogram
dendrogram(mergings,labels=companies,leaf_rotation=90,
           leaf_font_size=6)
plt.show()
