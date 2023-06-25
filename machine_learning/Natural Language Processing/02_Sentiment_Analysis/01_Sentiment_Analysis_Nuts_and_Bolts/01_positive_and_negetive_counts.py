"""How many positive and negative reviews are there?
As a first step in a sentiment analysis task, similar to other data science problems, we might want to explore the dataset in more detail.

You will work with a sample of the IMDB movies reviews. A dataset called movies has been created for you. It is a sample of the data we saw in the slides. Feel free to explore it in the IPython Shell, calling the .head() method, for example.

Be aware that this exercise uses real data, and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real data).

Instructions
100 XP
Find the number of positive and negative reviews in the movies dataset.
Find the proportion (percentage) of positive and negative reviews in the dataset."""

import pandas as pd

movies=pd.read_csv("IMDB_sample.csv")

# Find the number of positive and negative reviews
print('Number of positive and negative reviews: ', movies.label.value_counts())

# Find the proportion of positive and negative reviews
print('Proportion of positive and negative reviews: ', movies.label.value_counts() /len(movies))