"""More string operators and Twitter
In this exercise, you will apply different string operators to three strings, selected from the tweets dataset. A tweets_list has been created for you.

You need to construct three new lists by applying different string operators:

a list retaining only letters
a list retaining only characters
a list retaining only digits
The required functions have been imported for you from nltk.

Instructions
100 XP
Create a list of the tokens from tweets_list.
In the list letters remove all digits and other characters, i.e. keep only letters.
Retain alphanumeric characters but remove all other characters in let_digits.
Create digits by removing letters and characters and keeping only numbers."""

# Create a list of lists, containing the tokens from list_tweets

tweets_list=["@VirginAmerica it's really aggressive to blast obnoxious 'entertainment' in your guests' faces &amp; they have little recourse",
 "@VirginAmerica Hey, first time flyer next week - excited! But I'm having a hard time getting my flights added to my Elevate account. Help?",
 '@united Change made in just over 3 hours. For something that should have taken seconds online, I am not thrilled. Loved the agent, though.']

from nltk.tokenize import word_tokenize
tokens = [word_tokenize(item) for item in tweets_list]

# Remove characters and digits , i.e. retain only letters
letters = [[word for word in item if word.isalpha()] for item in tokens]
# Remove characters, i.e. retain only letters and digits
let_digits = [[word for word in item if word.isalnum()] for item in tokens]
# Remove letters and characters, retain only digits
digits = [[word for word in item if word.isdigit()] for item in tokens]

# Print the last item in each list
print('Last item in alphabetic list: ', letters[2])
print('Last item in list of alphanumerics: ', let_digits[2])
print('Last item in the list of digits: ', digits[2])