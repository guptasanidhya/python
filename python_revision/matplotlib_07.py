import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
gapminder =pd.read_csv('E:\study\Extra\python_rev\gapminder.csv',index_col=0)
# print(gapminder)

dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
country=gapminder.loc[:,'country']
cont=gapminder.loc[:,'cont']
npc=np.array(country)
npcont=np.array(cont)
colorcountry=[]
for con in npcont:
    colorcountry.append(dict[con])
pop=gapminder.loc[:,'population']
gdp_cap=gapminder.loc[:,['gdp_cap']]
life_exp=gapminder.loc[:,['life_exp']]
np_pop=np.array(pop)
np_col=np.column_stack((npc,colorcountry)) #contains nmupy list of[country,color]
# print(np_pop)
# print(pop.to_string(index=False),end="")
#we can directly use c=colorcountry at the place of np_col[:,1]
plt.scatter(x = gdp_cap, y = life_exp,s=np_pop/1000000,c=np_col[:,1],alpha=0.5)

# Previous customizations
plt.xscale('log')
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])
# Add grid() call
plt.grid(True)
plt.text(2400, 62.44, 'India')
plt.text(3500, 71.87, 'China')
# Show the plot
plt.show()
# Additional customizations
