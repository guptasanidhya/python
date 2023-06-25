"""Longest and shortest reviews
In this exercise, you will continue to work with the movies dataset. You explored how many positive and negative reviews there are. Now your task is to explore the review column in more detail.

Instructions 1/2
50 XP
Use the review column of the movies dataset to find the length of the longest review."""
import pandas as pd

movies=pd.read_csv("IMDB_sample.csv")
length_reviews = movies.review.str.len()

# How long is the longest review
print(max(length_reviews))

length_reviews = movies.review.str.len()

# How long is the shortest review
print(min(length_reviews))