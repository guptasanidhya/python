import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
artists=pd.read_csv('userdata.csv')
# print(artists)
user=artists.iloc[:,0]
a_number=np.array(artists.iloc[:,1]-1)
# print(a_number)##########################33
play=np.array(artists.iloc[:,2])
users=np.unique(user)
name=pd.read_csv("artists.csv")
names=name.iloc[:,0]
np_names=np.array(names)################################
# print(np_names)
#
data={
    'arname':np_names
}
df = pd.DataFrame(data)
df[users] = 0
"""
print(df)
print(user==0)
a=play[user==0]
print("no of counts user plays the song",a)
b=a_number[user==0]
print("index number of artist who is heard by user",b)
print(np_names[a_number[user==0]])"""
print(len(users))
for j in range(len(users)):#j is number of users
    song_count = play[user == j]#no of counts user plays the song
    artist_num = a_number[user == j]#"index number of artist who is heard by user"
    # print(a,b)
    for i in range(len(song_count)):
        sc=song_count[i]
        an=artist_num[i]
        # print(aa,bb)
        df.iloc[an,j+1]=sc#inserting values in the dataframe

print(df)
df.drop("arname",axis=1,inplace=True)
print(df)
