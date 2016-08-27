#All of the functions which I use for validation will be kept in here. 
def mainValid(choice):
  if choice == "y" or choice == "n":
    return True
  else:
    return False

def mainMenuValid(choice):
  if choice == 1:
    return True
  else: 
    return False 

def optionsValid(choice):
  if choice == 1 or choice == 2:
    return True
  else: 
    return False
    