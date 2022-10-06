# Import cars data
import pandas as pd
cars = pd.read_csv('car1.csv', index_col = 0)

# Extract drives_right column as Series: dr
# dr=cars.loc[:,'drives_right']

# Use dr to subset cars: sel
# ser=cars[dr]
ser=cars[cars.loc[:,'drives_right']]
# Print sel
print(ser)