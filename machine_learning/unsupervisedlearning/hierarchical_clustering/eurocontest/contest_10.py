# Perform the necessary imports
from scipy.cluster.hierarchy import linkage, dendrogram
from scipy.cluster.hierarchy import fcluster
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
samples=pd.read_csv('eurovision-2016.csv')
samples = samples.dropna(how='any')
country1=np.array(samples.iloc[:,0])
country2=np.array(samples.iloc[:,1])
samples.drop(columns = samples.columns[0:2], axis = 1, inplace= True)
# print(country2)
# print(samples)
# Calculate the linkage: mergings
mergings = linkage(samples,method='complete')
labels = fcluster(mergings, 15, criterion='distance')
print(labels)

# Plot the dendrogram, using varieties as labels
euro=['Albania (RTSH)','Armenia (AMPTV)','Australia (SBS)','Austria (ORF)','Azerbaijan (İTV)','Belarus (BTRC)','Belgium (VRT)','Bosnia and Herzegovina (BHRT)',
      'Bulgaria (BNT)','Croatia (HRT)','Cyprus (CyBC)','Czech Republic (ČT)','Denmark (DR)',
      'Estonia (ERR)','Finland (YLE)','France (France Télévisions)',
      'FYR Macedonia (MKRTV)','Georgia (GPB)','Germany (NDR)','Greece (ERT)','Hungary (MTVA)',
      'Iceland (RÚV)','Ireland (RTÉ)','Israel (IBA)',"Italy (RAI)",'Latvia (LTV)','Lithuania (LRT)',
      'Malta (PBS)','Moldova (TRM)','Montenegro (RTCG)','The Netherlands (AVROTROS)','Norway (NRK)',
      'Poland (TVP)','Romania (TVR)','Russia (RTR)','San Marino (SMRTV)','Serbia (RTS)',
      'Slovenia (RTVSLO)','Spain (TVE)','Sweden (SVT)','Switzerland (SRG SSR','Ukraine (NTU)',
      'United Kingdom (BBC)']
pairs = pd.DataFrame({'labels': labels,
'countries': country2})
print(pairs.sort_values('labels'))
print(pairs[labels==6])
dendrogram(mergings,
           labels=np.array(country2),
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()

"""
Different linkage, different hierarchical clustering!
In the video, you saw a hierarchical clustering of the voting countries at the Eurovision song contest using 'complete' linkage. Now, perform a hierarchical clustering of the voting countries with 'single' linkage, and compare the resulting dendrogram with the one in the video. Different linkage, different hierarchical clustering!

You are given an array samples. Each row corresponds to a voting country, and each column corresponds to a performance that was voted for. The list country_names gives the name of each voting country. This dataset was obtained from Eurovision.

Instructions
100 XP
Import linkage and dendrogram from scipy.cluster.hierarchy.
Perform hierarchical clustering on samples using the linkage() function with the method='single' keyword argument. Assign the result to mergings.
Plot a dendrogram of the hierarchical clustering, using the list country_names as the labels. In addition, specify the leaf_rotation=90, and leaf_font_size=6 keyword arguments as you have done earlier.
"""