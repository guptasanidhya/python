import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

artists = pd.read_csv('userdata.csv')
# print(artists)
user = artists.iloc[:, 0]
a_number = np.array(artists.iloc[:, 1] - 1)
# print(a_number)##########################33
play = np.array(artists.iloc[:, 2])
users = np.unique(user)
name = pd.read_csv("artists.csv")
names = name.iloc[:, 0]
np_names = np.array(names)  ################################
# print(np_names)
#
data = {
    'arname': np_names
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
# print(len(users))
for j in range(len(users)):  # j is number of users
    song_count = play[user == j]  # no of counts user plays the song
    artist_num = a_number[user == j]  # "index number of artist who is heard by user"
    # print(a,b)
    for i in range(len(song_count)):
        sc = song_count[i]
        an = artist_num[i]
        # print(aa,bb)
        df.iloc[an, j + 1] = sc  # inserting values in the dataframe

# print(df)
df.drop("arname", axis=1, inplace=True)
# print(df)
# Perform the necessary imports
from sklearn.decomposition import NMF
from sklearn.preprocessing import Normalizer, MaxAbsScaler
from sklearn.pipeline import make_pipeline

# Create a MaxAbsScaler: scaler
scaler = MaxAbsScaler()

# Create an NMF model: nmf
nmf = NMF(n_components=20)

# Create a Normalizer: normalizer
normalizer = Normalizer()

# Create a pipeline: pipeline
pipeline = make_pipeline(scaler, nmf, normalizer)

# Apply fit_transform to artists: norm_features
norm_features = pipeline.fit_transform(df)
# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=np_names)
print(df)
# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']
# print(artist)
print(artist.shape)
# Compute cosine similarities: similarities
"""computing similarities with the whole dataframe"""
similarities = df.dot(artist)
# print(similarities)
# Display those with highest cosine similarity
print(similarities.nlargest())
"""# Import pandas
import pandas as pd

# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=artist_names)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())
"""
"""
Recommend musical artists part I
In this exercise and the next, you'll use what you've learned about NMF to recommend popular music artists! You are given a sparse array artists whose rows correspond to artists and whose columns correspond to users. The entries give the number of times each artist was listened to by each user.

In this exercise, build a pipeline and transform the array into normalized NMF features. The first step in the pipeline, MaxAbsScaler, transforms the data so that all users have the same influence on the model, regardless of how many different artists they've listened to. In the next exercise, you'll use the resulting normalized NMF features for recommendation!
"""
