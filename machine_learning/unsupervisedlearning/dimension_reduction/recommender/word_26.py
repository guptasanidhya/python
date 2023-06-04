
import pandas as pd
from scipy.sparse import csr_matrix
"""
documents in row words in column so we have to transpose it to words in row and documents in column
"""
df = pd.read_csv('wikipedia-vectors.csv', index_col=0)
articles = csr_matrix(df.transpose())
titles = list(df.columns)
print(titles)
# Import NMF
from sklearn.decomposition import NMF

# Create an NMF instance: model
model = NMF(n_components=6)

# Fit the model to articles
model.fit(articles)

# Transform the articles: nmf_features
nmf_features = model.transform(articles)
# Perform the necessary imports
import pandas as pd
from sklearn.preprocessing import normalize
"""
Normalization is a scaling technique in Machine Learning applied during data preparation to change the
 values of numeric columns in the dataset to use a common scale. It is not necessary for all datasets
  in a model. It is required only when features of machine learning models have different ranges.
"""
# Normalize the NMF features: norm_features
norm_features = normalize(nmf_features)
print(norm_features)
# Create a DataFrame: df
df = pd.DataFrame(norm_features, index=titles)
print(df)
# Select the row corresponding to 'Cristiano Ronaldo': article
article = df.loc['Cristiano Ronaldo']
print(article.shape)
# Compute the dot products: similarities
similarities = df.dot(article)
# print(similarities)
# Display those with the largest cosine similarity
print(similarities.nlargest())

"""Which articles are similar to 'Cristiano Ronaldo'?
In the video, you learned how to use NMF features and the cosine similarity to find similar articles. Apply this to your NMF model for popular Wikipedia articles, by finding the articles most similar to the article about the footballer Cristiano Ronaldo. The NMF features you obtained earlier are available as nmf_features, while titles is a list of the article titles.

Instructions
100 XP
Instructions
100 XP
Import normalize from sklearn.preprocessing.
Apply the normalize() function to nmf_features. Store the result as norm_features.
Create a DataFrame df from norm_features, using titles as an index.
Use the .loc[] accessor of df to select the row of 'Cristiano Ronaldo'. Assign the result to article.
Apply the .dot() method of df to article to calculate the cosine similarity of every row with article.
Print the result of the .nlargest() method of similarities to display the most similar articles. This has been done for you, so hit 'Submit Answer' to see the result!
"""