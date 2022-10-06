import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import statistics

"""df =sns.load_dataset('tips')
print(df.head())
mean,median,mode
print(np.mean(df['total_bill']),np.median(df['total_bill']),statistics.mode(df['total_bill']))
sns.boxplot(df['total_bill'])
sns.histplot(df['total_bill'],kde=True)"""

df= sns.load_dataset('iris')
print(df.head())
# sns.histplot(df['sepal_length'],kde=True)
# sns.countplot(df['species'])
print(np.percentile(df['sepal_length'],[25,75]))
plt.show()