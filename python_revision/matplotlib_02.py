# Change the line plot below to a scatter plot
import matplotlib.pyplot as plt
gdp_cap=[1,2,3,4,5]
life_exp=[5,34,3,2,1]
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()