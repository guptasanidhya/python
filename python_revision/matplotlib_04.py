# Scatter plot
import matplotlib.pyplot as plt
import numpy as np
gdp_cap=np.round(np.random.normal(100000,50000,10),2)
life_exp=np.round(np.random.normal(60,20,10),2)
plt.scatter(gdp_cap, life_exp)

# Previous customizations
import matplotlib.pyplot as plt
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()