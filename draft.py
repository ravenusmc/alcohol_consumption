#Draft file, I test out ideas in here. 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#cols = ['Beer_Servings', 'Spirit_Servings', 'Wine_Servings', 'Total_Litres_of_Pure_Alcohol']
# drinks = pd.read_csv('drinks.csv', index_col="country")

drinks = pd.read_csv('drinks.csv')
#print(drinks.head())

#Seeing the data types of the data.
#print(drinks.dtypes)

#print(drinks[drinks.country])

print(drinks[['country', 'beer_servings']])
print(drinks[['beer_servings']])

page 150 Pandas book