import random
import sys

#our math project.
# Developed by avery b
# Assistance + math by Lauren C and James Z

#############################################################################################
#  MAY NOT BE FUNCTIONAL! THIS CODE IS ONLY ON GITHUB SO MY GROUP MEMBERS CAN ACCESS IT.    #
#############################################################################################

coin = False #using a boolean is easier, so: False = Tails, and True = Heads
debugMode = False #cool feature i want to add. False by default
balance = 5 # Your money. Default is 5.

def play(): # This is the play process
    if debugMode == True:
        print("")
    print("You have chosen [Play].")
    print("")
    print("")
    initial_flip = input("Press ENTER to flip coin.")
    coin_random = random.randint(0,100)
    if coin_random > 50:
        coin = False # Tails
        print("Tails!")
    else:
        coin = True # Heads
        print("Heads!")
    
    print("")

def main():
    print("Welcome Ultra Coin. Please chose from the following:")
    print("1. Play")
    print("2. Options")
    print("")
    ask1 = input(">")

    if ask1 == "1": 
        play()
    
def dev_mode():
    debugMode = True
    print("")
    print("Developer mode enabled.")
    print("")
    main()
