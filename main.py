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
  drinks = pd.read_csv('drinks.csv')
  print("Main Menu:")
  print("1. Beer Servings by country")
  choice = int(input("What is your choice? "))
  while not mainMenuValid(choice):
    print("Please enter an acceptable option!")
    choice = int(input("What is your choice? "))
  if choice == 1:
    beerServings(drinks)

def beerServings(drinks):
  print("\033c")
  print("Welcome to Beer Servings by Country")
  print("Here you will see which states have the most beer!")
  

main()
