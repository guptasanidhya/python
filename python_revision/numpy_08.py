import numpy as np
height=np.round(np.random.normal(1.75,0.20,5),2)
weight=np.round(np.random.normal(60.30,15,5),2)
np_height=np.array(height)
np_weight=np.array(weight)
# for h in np.nditer(np_height):
#     print(h)
# for w in np.nditer(np_weight):
#     print(w)
meas=np.array([np_height,np_weight])
print(meas)
print(meas[1,2])
# for val in np.nditer(meas):
#     print(val)
