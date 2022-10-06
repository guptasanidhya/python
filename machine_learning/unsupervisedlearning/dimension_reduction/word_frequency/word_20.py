import pandas as pd
from scipy.sparse import csr_matrix

df = pd.read_csv('wikipedia-vectors.csv', index_col=0)

articles = csr_matrix(df.transpose())
# print(articles)
titles = list(df.columns)
print(titles)
# Perform the necessary imports
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline

# Create a TruncatedSVD instance: svd
svd = TruncatedSVD(n_components=50)

# Create a KMeans instance: kmeans
kmeans = KMeans(n_clusters=6)

# Create a pipeline: pipeline
pipeline =make_pipeline(svd,kmeans)
print(df.head())
# print(articles)
# Import pandas
import pandas as pd

# Fit the pipeline to articles
pipeline.fit(articles)

# Calculate the cluster labels: labels
labels = pipeline.predict(articles)

# Create a DataFrame aligning labels and titles: df
df = pd.DataFrame({'label': labels, 'article': titles})

# Display df sorted by cluster label
print(df.sort_values('label'))

"""
As discussed above, it is a matrix factorization technique similar to PCA (principal component analysis).
 However, we perform Truncated SVD  or any SVD on the data matrix,
  whereas we use PCA on the covariance matrix.

Truncated SVD factorized data matrix where the number of columns is equal to the truncation.
 It drops the digits after the decimal place for shorting the value of float digits mathematically.
  For example, 2.498 can be truncated to 2.5.

 A given m⤫n matrix truncated SVD will produce matrices with the specified number of columns,
  whereas a normal SVD procedure will produce with m columns. It means that it will drop off all
   features except the number of features provided to it."""

"""
You saw in the video that TruncatedSVD is able to perform PCA on sparse arrays in csr_matrix format,
 such as word-frequency arrays. Combine your knowledge of TruncatedSVD and k-means to cluster some popular
  pages from Wikipedia. In this exercise, build the pipeline. In the next exercise, you'll apply it to
   the word-frequency array of some Wikipedia articles.

Create a Pipeline object consisting of a TruncatedSVD followed by KMeans.
 (This time, we've precomputed the word-frequency matrix for you, so there's no need for a TfidfVectorizer).

The Wikipedia dataset you will be working with was obtained from here."""

"""
It is now time to put your pipeline from the previous exercise to work!
 You are given an array articles of tf-idf word-frequencies of some popular Wikipedia articles,
  and a list titles of their titles. Use your pipeline to cluster the Wikipedia articles.

A solution to the previous exercise has been pre-loaded for you, so a Pipeline pipeline
 chaining TruncatedSVD with KMeans is available.
"""

