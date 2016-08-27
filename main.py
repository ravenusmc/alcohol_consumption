#This is the main file of the project. 
#Importing the libraries that will be used:
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

#using other files which I wrote for this program. 
from valid import *

#The main function which will launch the program. 
def main():
  print("\033c")
  print("---------------------------------------------")
  print("-----    Welcome to drinking data       -----")
  print("Where you see what countries drink the most!")
  print("{___________________________________________}")
  choice = input("Do you want to use the program?(y/n) ")
  while not mainValid(choice):
    choice = input("Do you want to use the program?(y/n) ")
  if choice == "y":
    mainMenu()
  elif choice == 'n':
    print("Thank you for using the program.")
    print("I hope that you use it soon!")

#This function is where I will actually pull the drinks data as well as let the user choose what 
#they want to do. 
def mainMenu():
  print("\033c")
  drinks = pd.read_csv('http://bit.ly/drinksbycountry')
  print("Main Menu:")
  print("1. Average drinks by Continent")
  choice = int(input("What is your choice? "))
  while not mainMenuValid(choice):
    print("Please enter an acceptable option!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    AvergeDrinksByContinent(drinks)

#This function will show the user the graph of the average drinks by continent. 
def AvergeDrinksByContinent(drinks):
  print("\033c")
  print("Welcome to average drinks by continent")
  print("Here you will see the average drinks by continent")
  print("Please not that in order to move on, you have to actually close the graph.")
  plt.show(drinks.groupby('continent').mean().plot(kind='bar'))
  mainOptions()

### Non critical functions: 

#This function is a generic function to allow the user to quit or to return to the main menu. 
def mainOptions():
  print("1. Main Menu")
  print("2. Quit")
  choice = int(input("What is your option? "))
  while not optionsValid(choice):
    print("That option is not allowed!")
    choice = int(input("What is your option? "))
  if choice == 1:
    mainMenu()
  elif choice == 2:
    print("Thank you for using the program!")
    print("Hope you come back soon!")

main()
