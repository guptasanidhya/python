
# inds_ascending = np.argsort(lr.coef_)
# inds_descending = inds_ascending[::-1]
#
# # Print the most positive words
# print("Most positive words: ", end="")
# for i in range(5):
#     print(vocab[inds_descending[i]], end=", ")
# print("\n")
#
# # Print most negative words
# print("Most negative words: ", end="")
# for i in range(5):
#     print(vocab[inds_ascending[i]], end=", ")
# print("\n")

"""
Identifying the most positive and negative words
In this exercise we'll try to interpret the coefficients of a logistic regression fit on the movie review sentiment dataset. The model object is already instantiated and fit for you in the variable lr.

In addition, the words corresponding to the different features are loaded into the variable vocab. For example, since vocab[100] is "think", that means feature 100 corresponds to the number of times the word "think" appeared in that movie review.

Instructions
0 XP
Find the words corresponding to the 5 largest coefficients.
Find the words corresponding to the 5 smallest coefficients.

Hint
inds_descending[0] contains the index of the largest coefficient.
vocab[inds_descending[0]] contains the word corresponding to the largest coefficient.
inds_ascending gives the words starting with the most negative, while inds_descending gives the opposite.
"""