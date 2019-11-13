import random
import sys

#our math project.
# Developed by avery b
# Assistance + math by Lauren C and James Z

#############################################################################################
#  MAY NOT BE FUNCTIONAL! THIS CODE IS ONLY ON GITHUB SO MY GROUP MEMBERS CAN ACCESS IT.    #
#############################################################################################

global coin
global balance
global debugMode
global build
coin = False #using a boolean is easier, so: False = Tails, and True = Heads
debugMode = False # False by default, deprecated at the moment.
balance = 10 # Your money. Default is 10.
build = 1 # build information since this will be compiled to an exe.

def heads():
    print("Since you got heads, you can 1 dice.")
    one_dice = input("Press ENTER to roll dice.")
    dice_random = random.randint(1,6)
    print("Your dice rolled a",dice_random)

def tails():
    print("Since you got heads, you can 2 die.")
    two_dice = input("Press ENTER to roll dice.")
    dice_random = random.randint(1,6)
    dice_random_2 = random.randint(1,6)
    print("Dice 1 rolled a",dice_random,", and dice 2 rolled a",dice_random_2,".")

def main():
    print("Welcome Ultra Coin. Please chose from the following:")
    print("1. Play")
    print("2. Options")
    print("")
    print("Your money: ",balance)
    ask1 = input(">")

    if ask1 == "1": 
        play()
    
# def dev_mode():
#     if debugMode == False:
#         debugMode = True
#     elif debugMode == True:
#         debugMode = False
#     print("")
#     print("Developer mode enabled.")
#     print("")
#     main()

def play(): # This is the play process
    # if debugMode == True:
    #     print("")
    print("You have chosen [Play].")
    print("")
    print("")
    initial_flip = input("Press ENTER to flip coin.")
    coin_random = random.randint(0,100)
    if coin_random > 50:
        coin = False # Tails
        print("Tails!")
        tails()
    else:
        coin = True # Heads
        print("Heads!")
        heads()
    
    print("")

main()
