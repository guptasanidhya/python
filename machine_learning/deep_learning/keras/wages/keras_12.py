import numpy as np
import pandas as pd
df=pd.read_csv('../titanic/titanic_all_numeric.csv')
print(df.describe())