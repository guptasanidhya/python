# Import cars data
import pandas as pd
cars = pd.read_csv('car1.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+":"+str(row['cars_per_cap']))
