#Draft file, I test out ideas in here. 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#cols = ['Beer_Servings', 'Spirit_Servings', 'Wine_Servings', 'Total_Litres_of_Pure_Alcohol']
# drinks = pd.read_csv('drinks.csv', index_col="country")

# drinks = pd.read_csv('drinks.csv')
#print(drinks.head())

#Seeing the data types of the data.
#print(drinks.dtypes)

#print(drinks[drinks.country])

#print(drinks[['country', 'beer_servings']])

# index = np.arange(192)
# bar_width = 0.25

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
#print(drinks.head())

#print(movies[(movies.duration > 200) & (movies.genre == 'Drama')])
#print((drinks[(drinks.continent == "Africa") & (drinks.beer_servings >= 1)]))
plt.show(drinks.groupby('continent').mean().plot(kind='bar'))

### CREATING A BAR GRAPH:

# stateList = drinks[['country']]
# beerList = drinks[['beer_servings']]

# stateArray = []
# beerArray = []

# i = 0
# while i < 193: 
#   state = stateList.iat[i,0]
#   beer = beerList.iat[i,0]
#   stateArray.append(state)
#   beerArray.append(beer)
#   i += 1 

# y_pos = np.arange(len(stateArray))

# plt.barh(y_pos, beerArray, align='center', alpha=0.5)
# plt.xticks(y_pos, stateList)
# plt.xlabel("State", fontsize=14)
# plt.ylabel("Beer Servings", fontsize=12)
# plt.title("Beer Servings by State", fontsize=16)
# plt.show()




















 

