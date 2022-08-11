EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

import random
guess = 0
COMPUTER_PICK = random.randint(1,100)

from art import logo
print(logo)

def compare(user_num,computer_num):
  if user_num > computer_num:
    print("Too high.")
  elif user_num < computer_num:
    print("Too low.")

def set_difficulty():
  while(1):
    level = input("Type 'easy' to pick an easy level with 10 guesses, or 'hard' to pick a hard level with 5 guesses.: ")
    if level == "easy":
      rounds = EASY_LEVEL_TURNS
      return rounds
    elif level == "hard":
      rounds = HARD_LEVEL_TURNS
      return rounds
    else:
      print("Invalid answer.")    

picks = set_difficulty()
for pick in range(picks):
  guess = int(input("Try to guess the number: "))
  if(guess==COMPUTER_PICK):
    break
  compare(guess,COMPUTER_PICK)
  if(picks-pick-1 != 0):
    if(picks-pick-1>1):
      print(f"You have {picks-pick-1} attempts remaining to guess the number.")
    else:
      print(f"You have {picks-pick-1} attempt remaining to guess the number.")

if(guess==COMPUTER_PICK):
    print(f"The number picked by the computer was {COMPUTER_PICK}.")
    print("You won.")
else:
  print(f"The number picked by the computer was {COMPUTER_PICK}.")
  print("You lost.")