import pandas as pd
import numpy as np
from sklearn.neighbors  import KNeighborsClassifier
dict={'0':'SepalLengthCm','1':'SepalWidthCm',
      '2':'PetalLengthCm','3':'PetalWidthCm'}
a=input( "'0':'SepalLengthCm','1':'SepalWidthCm'"
      " '2':'PetalLengthCm','3':'PetalWidthCm'\n"
      "use commas between numbers\n"
        "enter the values you don't have:")
values=[]
values.append(a.split(','))
feature=['Species','Id']
for i in range(len(values[0])):
      feature.append(dict[values[0][i]])
print(feature)
df =pd.read_csv('Iris.csv')
df.replace(('Iris-setosa','Iris-versicolor','Iris-virginica'),(0,1,2),inplace=True)
# print(df.head())
X=df.drop(feature,axis=1).values#axis-1 means columns
y=df['Species'].values

knn=KNeighborsClassifier(n_neighbors=7)
feature_values=input("Enter the feature values")
avai_features=feature_values.split(',')

for i in range(0, len(avai_features)):
    avai_features[i] = int(avai_features[i])

knn.fit(X,y)
print(knn.predict([avai_features]))