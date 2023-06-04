import pandas as pd
import numpy as np

df= pd.read_csv('house-votes-8.csv')
# print(df.shape)
# print(df.head())
df = df.drop(df.columns[0], axis=1)
# print(df)
# print(df.shape)
v=int(df.shape[1])
print(v)
# Get the frequency counts of 'category_var'
frequency_counts = df.iloc[:,1].value_counts()
#
#  Print the frequency counts
print(frequency_counts)

for i in range(v):
    column_values = df.iloc[:, i]
    column_values.replace(('y', 'n'), (1, 0), inplace=True)
    mode_value = column_values.mode()[0]
    column_values.replace('?', mode_value, inplace=True)

# Get the frequency counts of 'category_var'
frequency_counts = df.iloc[:,1].value_counts()
# Print the frequency counts
print(frequency_counts)

# print(df.head())
df=df.astype(float)
# print(df)
print(df.describe())