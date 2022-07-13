import random

rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
number_user = int(input("Type these numbers to choose a certain action: 0 - rock, 1 - paper, 2 - scissors. "))
number_computer = random.randint(0,2) 

if number_user == 0:
  number_user = rock
elif number_user == 1:
  number_user = paper
elif number_user == 2:
  number_user = scissors
else:
  print("You typed something else, you lost.")
  quit()

number_computer = random.randint(0,2)
if number_computer == 0:
  number_computer = rock
elif number_computer == 1:
  number_computer = paper
else:
  number_computer = scissors

if number_user == number_computer:
  victory = "draw."
elif number_user == paper and number_computer == rock:
  victory = "win."
elif number_user == rock and number_computer == scissors:
  victory = "win."
elif number_user == scissors and number_computer == paper:
  victory = "win."
else:
  victory = "lose."
  
print(f"You chose:\n {number_user}.")
print("\n")
print(f"The computer chose:\n {number_computer}")
print("\n")

if victory == "win." or victory == "lose.":
  print("You " + victory)
else:
  print("It's a " + victory)
