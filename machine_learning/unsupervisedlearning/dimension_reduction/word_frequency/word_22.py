
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
# print(model.components_)
# Print the NMF features
print(nmf_features.round(2))

# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(nmf_features,index=titles)
# Import pandas
import numpy as np

words = np.loadtxt("vocab.txt",dtype=str)
# print(File_data)
import pandas as pd
components_df = pd.DataFrame(model.components_)
print(components_df)
print("#################################################################################")
component = components_df.iloc[3]
# print(component)
# print("#################################################################################")
print(component.nlargest())
print("#################################################################################")
# Create a DataFrame: components_df
components_df = pd.DataFrame(model.components_,columns=words)
print(components_df)
# Print the shape of the DataFrame
print(components_df.shape)

# Select row 3: component
component = components_df.iloc[3]

# Print result of nlargest
print(component.nlargest())

"""
NMF learns topics of documents
In the video, you learned when NMF is applied to documents, the components correspond to topics of
 documents, and the NMF features reconstruct the documents from the topics. Verify this for yourself
  for the NMF model that you built earlier using the Wikipedia articles. Previously, you saw that the
   3rd NMF feature value was high for the articles about actors Anne Hathaway and Denzel Washington. 
   In this exercise, identify the topic of the corresponding NMF component.

The NMF model you built earlier is available as model, while words is a list of the words that label the columns of the word-frequency array.

After you are done, take a moment to recognize the topic that the articles about Anne Hathaway and Denzel Washington have in common!
"""