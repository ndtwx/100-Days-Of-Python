print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("WELCOME TO THE TREASURE ISLAND GAME!.")
print("YOUR MISSION IS TO FIND THE TREASURE!.\n")
print("******************************************************************************")
choice1 = input('Which path would you like to take? Type "left" or "right"\n')
if choice1 == "left":
    print("You chose the left path and reach the ocean.")
    print("******************************************************************************")
    choice2 = input('Would you like to swim over or wait for a boat? Type "swim" or "wait"\n')
    if choice2 == "wait":
        print("******************************************************************************")
        print("You chose to wait for the boat and reach the island safely")
        choice3 = input('Which door would you like to open. Type "red","yellow" or "blue"\n')
        if choice3 == "red":
            print("******************************************************************************")
            print("You got burn by the fire and died")
            print("GAME OVER")
            print("******************************************************************************")
        elif choice3 == "yellow":
            print("******************************************************************************")
            print("You found the treasure!")
            print("YOU WIN!")
            print("******************************************************************************")
        else:
            print("******************************************************************************")
            print("A beast rush out of the door and eat you up.")
            print("GAME OVER!")
            print("******************************************************************************")
    else:
        print("******************************************************************************")
        print("You tried to swim over but got killed by a gold fish.")
        print("GAME OVER!")
        print("******************************************************************************")
else:
    print("******************************************************************************")
    print("You chose the right path and fell into a hole")
    print("GAME OVER!")
    print("******************************************************************************")


