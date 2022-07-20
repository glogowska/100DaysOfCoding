import random
from hangman_art import *
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
lives = 6

#print(f'Pssst, the solution is {chosen_word}.')
display = []
for position in range(0,len(chosen_word)):
      display.append("_")
guesses = []
num_guesses = 0
while "_" in display:
    if(lives == 0):
      print("You lost.")
      print("The word was: " + chosen_word)
      break

    guess = input("Guess a letter: ").lower()
    num_guesses += 1
    #print(guesses)
    
    position = 0
    letter_exists = False
    letter_guessed = False
    for letter in chosen_word:
        if letter == guess:
            if(not display[position] == guess):
                display[position] = guess
                letter_exists = True
            else:
              letter_guessed = True
              letter_exists = True
        position +=1
    if letter_guessed == True:
      print("This letter has been already guessed.")
      
    if(not letter_exists):
        if not guess in guesses:
          lives -= 1
          print(stages[lives])
          guesses.append(guess)
        else:
          print("You have already typed this letter, try a different one.")
    else:
        print(f"{' '.join(display)}")
      
if(lives > 0):
    print("you won.")