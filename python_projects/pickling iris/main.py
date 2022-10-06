import requests
import pickle
"""
data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

# l1 = data.split("\n")
# print(l1)
"""
#taking data in text file
response=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
datafile=open("response.txt",'w')
datafile.writelines(response)
datafile.close()

with open("response.txt") as f:
    filelist=f.read().split("\n")

ls=[item.split(",") for item in filelist if len(item)!=0]
print(ls)

#pickling data into file

file="pfile.pkl"
fileobj=open(file,'wb')
irisfile=pickle.dump(ls,fileobj)
fileobj.close()

#pickling data from file

# fileobj=open("pfile.pkl",'rb')
# irisdata=pickle.load(fileobj)
# print(irisdata)
# print(type(irisdata))

