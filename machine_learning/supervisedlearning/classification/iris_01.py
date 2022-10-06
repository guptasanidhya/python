import pandas as pd
import numpy as np
from sklearn.neighbors  import KNeighborsClassifier
dict={'0':'SepalLengthCm','1':'SepalWidthCm',
      '2':'PetalLengthCm','3':'PetalWidthCm'}
a=input( "'0':'SepalLengthCm','1':'SepalWidthCm'"
      " '2':'PetalLengthCm','3':'PetalWidthCm'\n"
      "use commas between \n"
        "enter the values you have:")
values=[]
values.append(a.split(','))
feature=[]
for i in range(len(values[0])):
      feature.append(dict[values[0][i]])
print(feature)
df =pd.read_csv('Iris.csv')
df.replace(('Iris-setosa','Iris-versicolor','Iris-virginica'),(0,1,2),inplace=True)
# print(df.head())
X=df.loc[:,feature].values
print(X)
y=df['Species'].values

knn=KNeighborsClassifier(n_neighbors=7)

knn.fit(X,y)
print(knn.predict([[5.0,3.3,1.4]]))