"""
Step 3: Building a classifier
This is the last step in the sentiment analysis prediction. We have explored and enriched our dataset with features related to the sentiment, and created numeric vectors from it.

You will use the dataset that you built in the previous steps. Namely, it contains a feature for the length of reviews, and 200 features created with the Tfidf vectorizer.

Your task is to train a logistic regression to predict the sentiment. The data has been imported for you and is called reviews_transformed. The target is called score and is binary : 1 when the product review is positive and 0 otherwise.

Train a logistic regression model and evaluate its performance on the test data. How well does the model do?

All the required packages have been imported for you.

Instructions
100 XP
Perform the train/test split, allocating 20% of the data to testing and setting the random seed to 456.
Train a logistic regression model.
Predict the class.
Print out the accuracy score and the confusion matrix on the test set.
"""

from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
import pandas as pd

reviews=pd.read_csv("amazon_reviews_sample.csv")

# Tokenize each item in the review column
word_tokens = [word_tokenize(review) for review in reviews.review]

# Create an empty list to store the length of the reviews
len_tokens = []

# Iterate over the word_tokens list and determine the length of each item
for i in range(len(word_tokens)):
     len_tokens.append(len(word_tokens[i]))

# Create a new feature for the lengh of each review
reviews['n_words'] = len_tokens
print("######################################################## original task")
# Import the TfidfVectorizer and default list of English stop words
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS,TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# Build the vectorizer
vect = TfidfVectorizer(stop_words=ENGLISH_STOP_WORDS, ngram_range=(1, 2), max_features=200, token_pattern=r'\b[^\d\W][^\d\W]+\b').fit(reviews.review)
# Create sparse matrix from the vectorizer
X = vect.transform(reviews.review)

# Create a DataFrame
reviews_transformed = pd.DataFrame(X.toarray(), columns=vect.get_feature_names())
print('Top 5 rows of the DataFrame: \n', reviews_transformed.head())

# Define X and y
y = reviews['score']
X = reviews_transformed

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=456)

# Train a logistic regression
log_reg = LogisticRegression().fit(X_train,y_train)
# Predict the labels
y_predicted = log_reg.predict(X_test)

# Print accuracy score and confusion matrix on test set
print('Accuracy on the test set: ', accuracy_score(y_test, y_predicted))
print(confusion_matrix(y_test,y_predicted)/len(y_test))