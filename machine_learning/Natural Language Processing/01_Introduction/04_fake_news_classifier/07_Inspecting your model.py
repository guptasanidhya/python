import pandas as pd
df= pd.read_csv("fake_or_real_news.csv")
# print(df.head())

# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split


# Initialize a TfidfVectorizer object: tfidf_vectorizer
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
"""max_df=0.7 ignores terms that appear in more than 70% of the documents."""
# Create a series to store the labels: y
y = df.label
# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(df["text"],y,test_size=0.33,random_state=53)


# Transform the training data: tfidf_train
tfidf_train = tfidf_vectorizer.fit_transform(X_train)

# Transform the test data: tfidf_test
tfidf_test = tfidf_vectorizer.transform(X_test)

# Import the necessary modules
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB


# Create a Multinomial Naive Bayes classifier: nb_classifier
nb_classifier = MultinomialNB()

# Fit the classifier to the training data
nb_classifier.fit(tfidf_train,y_train)

# Create the predicted tags: pred
pred = nb_classifier.predict(tfidf_test)


"""_____________________________________________"""

# Get the class labels: class_labels
class_labels = nb_classifier.classes_
# Extract the features: feature_names
feature_names = tfidf_vectorizer.get_feature_names()

# Zip the feature names together with the coefficient array and sort by weights: feat_with_weight
#it will create a tuple
# feat_with_weights_class1 = sorted(zip(nb_classifier.feature_log_prob_[0], feature_names))
feat_with_weights_class1 = sorted(zip(nb_classifier.feature_log_prob_[1], feature_names))
feat_with_weights_class2 = sorted(zip(nb_classifier.feature_log_prob_[1], feature_names))

# Print the first class label and the top 20 feat_with_weights entries
print(class_labels[0], feat_with_weights_class1[:20]) #fake class

# Print the second class label and the bottom 20 feat_with_weights entries
print(class_labels[1], feat_with_weights_class2[-20:]) #real class