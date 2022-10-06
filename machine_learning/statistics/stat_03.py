"""
suppose the IQ in a certain population is normally distributed with a mean of 100 and std deviation of 15. A researcher
wants to know if a new drug affevts IQ levels ,so he recruits 20 patients to try it and records their iq levels

the following code shows how to perform a one sample z-test in pytohn to determine if the new drug causes a significant
difference in IQ levels:
"""
from statsmodels.stats.weightstats import ztest as ztest
data=[88,92,94,94,96,97,97,97,99,99,105,109,109,109,110,112,112,113,114,115]
import numpy as np
mean= np.mean(data)
print(mean)
print(ztest(data,value=100))
#z-test value ,p test value