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
    global playerInventory, playerStamina
    print()
    print("Name:", playerName)
    print("HP:", playerHP)
    print("Stamina", playerStamina)
    print("Inventory:", playerInventory)
    if "Mountain Dew" in playerInventory:
        print("Would you like to do the Dew?")
        choice = input(">")
        if choice == "yes" or choice == "y":
            playerStamina = playerStamina + 15
            print("You did the dew and the sugar rush gave you +15 stamina.")
            playerInventory.remove("Mountain Dew")
        time.sleep(3)

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
    print("2. Go to the dining room")
    print("3. Open the fridge")
    print("4. See my stats")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        diningRoom()
    elif choice == "3":
        if "Moutain Dew" not in playerInventory:
            print("You opened the fridge and found a bottle of Mountain Dew. Would you like to take it?")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("Mountain Dew")
                print("You took the Mountain Dew")
                time.sleep(3)
                kitchen()
            else:
                print("Your opened the fridge and found nothing")
        else:
            print("You searched the whole room and found nada")
            time.sleep(3)
            porch()
    elif choice == "4":
        showStats()
        time.sleep(3)
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
    print("2. Search the porch")
    print("3. See my stats")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        if "ded spider" not in playerInventory:
            print("You found a ded spider. Wanna pick it up??")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("ded spider")
                print("You picked up a depressing and dead spider...")
            else:
                print("You searched the whole room and found nada")
            time.sleep(3)
            porch()
    elif choice == "3":
        showStats()
        time.sleep(3)
        porch()
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
    print("3. Read a book")
    print("4. See my stats")
    choice = input(">")
    if choice == "1":
        livingRoom()
    elif choice == "2":
        kitchen()
    elif choice == "3":
        print("You grab a book off the bookshelf and unknowingly reveal a secret door")
        print("Would you like to open the door?")
        choice = inout (">")
        if choice == "yes" or choice == "y":
            if "friendly ghost" in playerInventory:
                escape()
            else:
                print("You find that the door is locked and there is no key")
                time.sleep(3)
                diningRoom()
        else:
            diningRoom()
    elif choice == "4":
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
    print("3. Search")
    print("4. See my stats")
    choice = input(">")
    if choice == "1":
        bedroom()
    elif choice == "2":
        pass
    elif choice == "3":
        if "friendly ghost" not in playerInventory:
            print("You found a friendly ghost. Do you want to be besties with the ghost?")
            choice = input(">")
            if choice == "y" or choice == "yes":
                playerInventory.append("friendly ghost")
                print("The ghost has begun to follow you around")
            time.sleep(3)
            bathroom()
        else:
            print("You searched tiresly and found absolutly... nothing")
            bathroom()
    elif choice == "4":
        showStats()
        time.sleep(4)
        bathroom()
    else:
        print("Bro, you can't do that ._.")
        time.sleep(4)
        bathroom()

def escape():
    print("Your friendly ghost phases through the locked door and unlocks it for you")
    print("You open the door and you see a way out but a ghostly shape is blocking the way")
    print("You look up in horror as you see a Dementor looking down upon you")
    if "book" in playerInventory:
        print("Your book starts to glow and opens up to reveal the spell for Expecto Patronum")
        print("The book summons a wand and you wave it yelling the words at the top of your lungs")
        print("I blinding light expels the Dementor and the exit is unblocked")
    else:
        print("You don't know how to dispel the dementor and it takes 50HP")
        playerHP = playerHP - 50
        print("You are teleported back to the living room")
        time.sleep(2)
        playerInventory.clear()
        livingRoom()
start()