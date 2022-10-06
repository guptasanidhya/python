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
print(np_pop/1000000000)