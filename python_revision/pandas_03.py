# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("car1.csv",index_col=0,encoding='latin1')

# Print out cars
print(cars)
print(cars.shape)

"""Run the code with Run Code and assert that the first column should actually be used as row labels.
Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
Has the printout of cars improved now?"""
