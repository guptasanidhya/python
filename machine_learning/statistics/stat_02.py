#finding the outliers
import numpy as np
dataset=[11,10,12,14,12,15,14,13,15,102,12,14,17,19,107,10,13,12,14,14,12,108,12,11,14,13,15,12,10,14,13,15,10]
"""outliers=[]

def detect_outliers(data):
    threshold=3
    mean=np.mean(data)
    std= np.std(data)
    for i in data:
        z_score=(i-mean)/std

        if np.abs(z_score)>threshold:
            outliers.append(i)
    return outliers

detected=detect_outliers(dataset)
print(detected)"""

"""USing IQR

1. sort the data
2.calculate q1 and q3
3.IQR(Q3-Q1)
4.find the lower fence (q1-1.5(iqr))
5.find the upper fence(q3+1.5(iqr))
"""
# dataset=sorted(dataset)
# print(dataset)
# q1,q3=np.percentile(dataset,[25,75])
# print(q1,q3)
# iqr=q3-q1
# lf=q1-(1.5*iqr)
# uf=q3+(1.5*iqr)
# print("lower fence:","\n",lf,"upper fence:",uf)


"""using the seaborn"""
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(dataset)
plt.show()