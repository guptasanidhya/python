# Import cars data
import pandas as pd
cars = pd.read_csv('car1.csv', index_col = 0)


# Iterate over rows of cars
for lab,rows in cars.iterrows():
    print(lab)
    print(rows)