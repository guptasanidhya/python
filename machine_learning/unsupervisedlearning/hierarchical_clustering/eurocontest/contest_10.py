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