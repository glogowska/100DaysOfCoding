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
print("Welcome to Treasure Island.")
print("You are in an abandoned house in the middle of the jungle. \nYour mission is to find the treasure.")
direction = (input("You walk out the door, do you want to go left or right? ")).lower()
print("\n\n")

if(direction == "left"):
  print("You fell into a trap. \nGAME OVER")
elif(direction == "right"):
  print("There is something on the tree! It's a big kitty.")
  print('''
  *******************************************************************************
             _      _
             (c\-.--/a)
              |q: p   /\_            _____
            __\(_/  ).    ---._.---`     "---.__
           /  (Y_)_/             /        : \-._ \
   !!!!,,, \_)) "-";             (       _/   \  \\_
  !!II!!!!!IIII,, \_             \     /      \_  .\
   !IIsndIIIII!!!!,,\     /_      \   |----.___ -. \".__
   !!!IIIIIIIIIIIIIIII\   | "--._.-  _)       \  |  `--
          !!!!IIIIIII/   .",, ((___.-         / /
                !!!!/  _/!!!!IIIIIII!!!!!,,,,,;,;,,,.....
                   | /IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                   | \   IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
                   \_,)     !!!!IIIIIIIIIIIIIIII!!!!!!!!
                                     !!!!!!!!!!!!!!!
  *******************************************************************************
  ''')
  direction = (input("Type P if you want to pet the lioness or R if you want to run. ")).lower()  
  if direction == "p":
    print("The kitty was very nice and showed you where to find the treasure.\nYou won the game! \nCONGRATULATIONS")
  elif direction == "r":
    print("You got lost in the jungle. \nGAME OVER")
  else:
    print("Something went wrong and you didn't respond properly, so you died:) \nGAME OVER") 
else:
  print("Something went wrong and you didn't respond properly, so you died:) \nGAME OVER")