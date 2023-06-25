"""
Your first BOW
A bag-of-words is an approach to transform text to numeric form.

In this exercise, you will apply a BOW to the annak list before moving on to a larger dataset in the next exercise.

Your task will be to work with this list and apply a BOW using the CountVectorizer(). This transformation is your first step in being able to understand the sentiment of a text. Pay attention to words which might carry a strong sentiment.

Remember that the output of a CountVectorizer() is a sparse matrix, which stores only entries which are non-zero. To look at the actual content of this matrix, we convert it to a dense array using the .toarray() method.

Note that in this case you don't need to specify the max_features argument because the text is short.

Instructions
100 XP
Import the count vectorizer function from sklearn.feature_extraction.text.
Build and fit the vectorizer on the small dataset.
Create the BOW representation with name anna_bow by calling the transform() method.
Print the BOW result as a dense array.

"""
# Import the required function
from sklearn.feature_extraction.text import CountVectorizer

annak = ['Happy families are all alike;', 'every unhappy family is unhappy in its own way']

# Build the vectorizer and fit it
anna_vect = CountVectorizer()
anna_vect.fit(annak)

# Create the bow representation
anna_bow = anna_vect.transform(annak)

# Print the bag-of-words result
print(anna_bow.toarray())