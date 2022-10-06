import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
columnnames=['party','handicapped-infants','water-project-cost-sharing','adoption-of-the-budget-resolution',
                       'physician-fee-freeze',' el-salvador-aid','religious-groups-in-schools','satellite',
                       'aid-to-nicaraguan-contras',' missile','immigration','synfuels-corporation-cutback',
                       'education-spending','superfund-right-to-sue','crime','duty-free-exportsduty-free-exports',
                       'export-administration-act-south-africa']
df=pd.read_csv("house-votes-8.csv", names=columnnames)
df.replace(('y','n','?'),(1,0,np.NAN,),inplace=True)
print(df.shape)
print(df)
plt.figure()
sns.countplot(x='education-spending', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()

'''Visual EDA
The Numerical EDA you did in the previous exercise gave you some very important information, such as the names and data types of the columns, and the dimensions of the DataFrame. Following this with some visual EDA will give you an even better understanding of the data. In the video, Hugo used the scatter_matrix() function on the Iris data for this purpose. However, you may have noticed in the previous exercise that all the features in this dataset are binary; that is, they are either 0 or 1. So a different type of plot would be more useful here, such as Seaborn's countplot.

Given on the right is a countplot of the 'education' bill, generated from the following code:

plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()
In sns.countplot(), we specify the x-axis data to be 'education', and hue to be 'party'. Recall that 'party' is also our target variable. So the resulting plot shows the difference in voting behavior between the two parties for the 'education' bill, with each party colored differently. We manually specified the color to be 'RdBu', as the Republican party has been traditionally associated with red, and the Democratic party with blue.

It seems like Democrats voted resoundingly against this bill, compared to Republicans. This is the kind of information that our machine learning model will seek to learn when we try to predict party affiliation solely based on voting behavior. An expert in U.S politics may be able to predict this without machine learning, but probably not instantaneously - and certainly not if we are dealing with hundreds of samples!'''