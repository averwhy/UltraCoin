import random, sys, time, re
import sqlite3
import os.path

# our math project.
# Developed by avery b
# Assistance + math by Lauren C and James Z

coin = False #using a boolean is easier, so: False = Tails, and True = Heads
build = 1 # build information since this will be compiled to an exe.
balance = None # Used for storing the read data from the database. Default is None. Please don't change this.
playing = None # used to manage balancing
dice_random = 0
dice_random_2 = 0

#########################################################################################################
# THE FOLLOWING CODE CHECKS FOR YOUR SAVE FILE. IF YOU REMOVE/EDIT/MOVE ANY OF IT, THE GAME WILL FAIL!
if os.path.isfile('playerdata.db'):
    print("================\nSave file located.\n================\n")
    db_exists = True
    conn = sqlite3.connect('playerdata.db')
    c = conn.cursor()
else:
    conn = sqlite3.connect('playerdata.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE playerdata
             (money text)''')
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("A new save file was created as the file 'playerdata.db'. IF YOU DELETE THIS FILE, YOU WILL LOSE YOUR DATA!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    c.execute("INSERT INTO playerdata VALUES ('10')")

conn.commit()
#########################################################################################################
# Well i guess if you removed/edit/move ANY of this is will fail too, but above is pretty important.

def heads():
    conn.commit()
    global dice_random
    global dice_random_2
    dice_random = 0
    dice_random_2 = 0
    print("Since you got heads, you can 1 dice.")
    input("Press ENTER to roll dice.")
    dice_random = random.randint(1,6)
    print("Your dice rolled a",dice_random)
    home()

def tails():
    conn.commit()
    global dice_random
    global dice_random_2
    dice_random = 0
    dice_random_2 = 0
    print("Since you got heads, you can 2 die.")
    input("Press ENTER to roll dice.")
    dice_random = random.randint(1,6)
    dice_random_2 = random.randint(1,6)
    print("Dice 1 rolled a",dice_random,", and dice 2 rolled a",dice_random_2,".")
    home()

def quit_():
    global conn
    conn.commit()
    conn.close()
    print("Thanks for playing!") # this never prints but whatever

def play(): # This is the play process
    global playing
    conn.commit()
    playing = True
    print("You have chosen [Play].")
    print("")
    print("")
    initial_flip = input("Press ENTER to flip coin.\n")
    coin_random = random.randint(0,100)
    if coin_random >= 50:
        coin = False # Tails
        print("Tails!")
        tails()
    else:
        coin = True # Heads
        print("Heads!")
        heads()

def home():
    global balance
    global playing
    global c
    c.execute('SELECT * FROM playerdata')
    data = c.fetchall()
    data = str(data)
    balance = int(re.search(r'\d+', data).group())
    conn.commit()

    if playing == True:
        result_math = balance + (dice_random + dice_random_2)
        sql_update_query = "Update playerdata set money = " + str(result_math) + " where money = " + str(balance)
        c.execute(sql_update_query)
        balance = balance + (dice_random + dice_random_2) #Adding to balance locally is important too
        conn.commit() # Save changes
        print("\nAdded",(dice_random + dice_random_2), "dollars to your account.")
        playing = False #So they cant spoof money earnings

    print("Welcome UltraCoin. Please choose from the following:")
    print("1. Play (Costs 7 dollars)")
    print("2. Reset")
    print("3. Quit")
    print("Your money:",balance)
    ask1 = input(">")

    if ask1 == "1":
        print("Deducted 7 dollars for cost of the game.")
        sql_update_query = "Update playerdata set money = " + str((balance - 7)) + " where money = " + str(balance)
        c.execute(sql_update_query)
        play()

    elif ask1 == "2":
        print("Are you sure you want to reset your balance?")
        print("The program will close if you proceed.")
        ask_reset = input("[Y/N] >")
        if ask_reset == "Y" or "y":
            print("Reseting your balance...")
            time.sleep(1)
            sql_update_query = "Update playerdata set money = 10 where money = " + str(balance)
            c.execute(sql_update_query)
            c.execute('SELECT * FROM playerdata')
            data = c.fetchall()
            data = str(data)
            balance = int(re.search(r'\d+', data).group())
            conn.commit()
            print("Data reset. New balance:",balance,".")
            time.sleep(0.5)
            print("Now closing...")
            quit()
        if ask_reset == "N" or "n":
            print("")
            home()

    elif ask1 == "3": 
        quit()
    else:
        ("Invalid character entered.\n\n")
        home()
    
home()
