# Import cars data
import pandas as pd
cars = pd.read_csv('car1.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np
# Create medium: observations with cars_per_cap between 100 and 500
cpc=cars.iloc[:,2]
between=np.logical_and(cpc>100,cpc<500)
medium=cars[between]
# Print medium
print(medium)

"""Remember about np.logical_and(), np.logical_or() and np.logical_not(),
 the NumPy variants of the and, or and not operators? You can also use them on Pandas Series to do more advanced filtering operations.

Take this example that selects the observations that have a cars_per_cap between 10 and 80. Try out these lines of code step by step to see what's happening.

cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]"""