import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
movements=pd.read_csv('company-stock.csv')
companies=np.array(movements.iloc[:,0])
print(movements)
movements.drop(columns = movements.columns[0], axis = 1, inplace= True)
# Create a normalizer: normalizer
normalizer = Normalizer()

# Create a KMeans model with 10 clusters: kmeans
kmeans = KMeans(n_clusters=10)

# Make a pipeline chaining normalizer and kmeans: pipeline
pipeline = make_pipeline(normalizer,kmeans)

# Fit pipeline to the daily price movements
pipeline.fit(movements)
labels = pipeline.predict(movements)
print(labels)

# Create a DataFrame aligning labels and companies: df
df = pd.DataFrame({'labels': labels, 'companies': companies})

# Display df sorted by cluster label
print(df.sort_values('labels'))


# companies=['Apple','AIG','Amazon','American express,Boeing','Bank of America','British American Tobacco','Canon','Caterpillar',
#            'Colgate-Palmolive','ConocoPhillips','Cisco','Chevron','DuPont de Nemours','Dell','Ford','General Electrics',
#            'Google/Alphabet','Goldman Sachs','GlaxoSmithKline','Home Depot','Honda','HP','IBM','Intel','Johnson & Johnson',
#            'JPMorgan Chase','Kimberly-Clark','Coca Cola','Lookheed Martin','MasterCard','McDonalds','3M','Microsoft',
#            'Mitsubishi','Navistar','Northrop Grumman','Novartis','Pepsi,Pfizer','Procter Gamble','Philip Morris',
#            'Royal Dutch Shell','SAP','Schlumberger','Sony','Sanofi-Aventis','Symantec','Toyota',
#            'Total','Taiwan Semiconductor Manufacturing','Texas instruments','Unilever,Valero Energy',
#            'Walgreen','Wells Fargo','Wal-Mart','Exxon','Xerox','Yahoo']