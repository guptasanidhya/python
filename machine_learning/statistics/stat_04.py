import numpy as np
ages=[10,20,35,50,28,40,55,18,16,55,30,25,43,18,30,28,14,24,16,17,32,35,26,27,65,18,43,23,21,20,19,70]
mean=np.mean(ages)
print(mean)
sample_size=10
sample=np.random.choice(ages,sample_size)
print(sample)
sample_mean=np.mean(sample)
print(sample_mean)
from scipy.stats import ttest_1samp
ttest=ttest_1samp(sample,mean)
print(ttest)
