"""
consider another example
ages of the college students(population)
#class student mean of all the ages
"""
import numpy as np
import pandas as pd
import math
import scipy.stats as stats
np.random.seed(6)
school_ages=stats.poisson.rvs(loc=18,mu=35,size=1500)
classA_ages=stats.poisson.rvs(loc=18,mu=30,size=60)
print(school_ages,school_ages.mean())
print(classA_ages,classA_ages.mean())

from scipy.stats import ttest_1samp
_,pvalue=ttest_1samp(classA_ages,school_ages.mean())
print(pvalue)
if pvalue<=0.05:
    print("reject h0")
else:
    print("accept it")