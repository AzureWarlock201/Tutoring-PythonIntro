import os, time

playerName = ""
playerHP = 100
playerInventory = []
playerStamina = 100

def start():
    global playerName
    print("Welcome to the Escape Game! ;)")
    print("What would you like your player to be called?")
    playerName = input (">")
    print("Welcome,", playerName)
    livingRoom()

def showStats ():
    print()
    print("Name:", playerName)
    print("HP:", playerHP)
    print("Stamina", playerStamina)
    print("Inventory:", playerInventory)
    time.sleep(4)

def livingRoom():
    os.system('clear')
    print("You are in the living room")
    print("Your options are:")
    print("1. Go to the kitchen")
    print("2. Go to the bedroom")
    print("3. Go to the porch")
    print("4. Go to the dining room")
    print("5. Search")
    print("6. See my stats")
    choice = input(">")
    if choice == "1":
        kitchen()
    elif choice == "2":
        bedroom()
    elif choice == "3":
        porch()
    elif choice == "4":
        diningRoom()
    elif choice == "5":
        print("You searched the whole room and found nothing. ;)")
        time.sleep(3)
        livingRoom()
    elif choice == "6":
        showStats()
        livingRoom()

    else:
        print("Bro, what? You can't do that -_-!")
        time.sleep(3)
        livingRoom()

def kitchen():
    os.system('clear')
    print("You are in the kitchen")
    print("Your options are:")
    print("1. Go back to the living room")
    print("2. Go to the kitchen")
    print("3. See my stats")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        kitchen()
    elif choice == "3":
        showStats()
        kitchen()
    else:
        print("Bro, what?")
        time.sleep(3)
        kitchen()

def bedroom():
    global playerStamina, playerInventory
    os.system('clear')
    print("You are in the bedroom")
    print("Your options are:")
    print("1. Go to the living room")
    print("2. Go to the bathroom")
    print("3. Sleep")
    print("4. Search")
    print("5. See my stats")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        bathroom()
    elif choice == "3":
        print("You lay down on the bed to take a nap. *_*")
        time.sleep(4)
        playerStamina += 10
        print("Congrats! You earned 10 stamina points! ^-^")
        time.sleep(3)
        bedroom()
    elif choice == "4":
        if "mysterious book" not in playerInventory:
            print("You found a book. Wanna pick it up??")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("mysterious book")
                print("You picked up a mysterious book...")
        else:
            print("You searched the whole room and found nothing...")
        time.sleep(3)
        bedroom()
        print("")
    elif choice == "5":
        showStats()
        livingRoom()
    else:
        print("Bro, what? You can't do that! -_-")
        time.sleep(3)
        bedroom()

def porch():
    os.system('clear')
    print("You are on the porch")
    print("Your options are:")
    print("1. Go to the living room")
    print("2. See my stats")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        showStats()
    else:
        print("Bro, you can't do that ._.")
        time.sleep(4)
        porch()

def diningRoom():
    os.system('clear')
    print("You are in the dining room")
    print("Your options are:")
    print("1. Go to the living room")
    print("2. Go on the kitchen") 
    print("3. See my stats")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        kitchen()
    elif choice == "3":
        showStats()
    else:
        print("Bro, you can't do that ._.")
        time.sleep(4)
        diningRoom()

def bathroom():
    os.system('clear')
    print("You are in the bedroom")
    print("Your options are:")
    print("1. Go to the bedroom")
    print("2. Go on the toilet") 
    print("3. See my stats")
    choice = input(">")
    if choice == "1":
        bedroom()
    elif choice == "2":
        pass
    elif choice == "3":
        showStats()
    else:
        print("Bro, you can't do that ._.")
        time.sleep(4)
        bathroom()


start()