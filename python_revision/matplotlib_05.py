# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt

pop=np.round(np.random.normal(100,50,10))
gdp_cap=np.round(np.random.normal(100000,50000,10),2)
life_exp=np.round(np.random.normal(70,5,10),2)
# Store pop as a numpy array: np_pop

np_pop=np.array(pop)

# Double np_pop
np_pop=np_pop*2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()