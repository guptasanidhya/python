# Import numpy and pandas
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Read the CSV file into a DataFrame: df
df = pd.read_csv("gm_2008_region.csv")
print(df.info())
print(df.describe())
print(df.head())
print(df.shape)
sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
plt.show()