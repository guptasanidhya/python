import numpy as np
#argument for np.random.normal()
"""distribution mean
distribution standard deviation
number of samples"""
height=np.round(np.random.normal(1.75,0.20,50),2)
weight=np.round(np.random.normal(60.30,15,50),2)
np_city=np.column_stack((height,weight))
print(np_city)
