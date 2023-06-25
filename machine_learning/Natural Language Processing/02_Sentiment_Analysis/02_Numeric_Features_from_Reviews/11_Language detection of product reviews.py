"""Language detection of product reviews
You will practice language detection on a small dataset called non_english_reviews. It is a sample of non-English reviews from the Amazon product reviews.

You will iterate over the rows of the dataset, detecting the language of each row and appending it to an empty list. The list needs to be cleaned so that it only contains the language of the review such as 'en' for English instead of the regular output en:0.9987654. Remember that the language detection function might detect more than one language and the first item in the returned list is the most likely candidate. Finally, you will assign the list to a new column.

The logic is the same as used in the slides and the exercise before but instead of applying the function to a list, you work with a dataset.

Instructions
100 XP
Iterate over the rows of the non_english_reviews dataset.
Inside the loop, detect the language of the second column of the dataset.
Clean the string by splitting on a : inside the list comprehension expression.
Finally, assign the cleaned list to a new column."""


from langdetect import detect_langs
languages = []


# Loop over the rows of the dataset and append
# for row in range(len(non_english_reviews)):
#     languages.append(detect_langs(non_english_reviews.iloc[row, 1]))
#
# # Clean the list by splitting
# languages = [str(lang).split(':')[0][1:] for lang in languages]
#
# # Assign the list to a new feature
# non_english_reviews['language'] = languages
#
# print(non_english_reviews.head())