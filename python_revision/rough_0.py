import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv("Round_of_8_2_2_Olympics.csv")
print(df)
aa=df['countries'].count().unique()
print(aa)
