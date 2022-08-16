import random
from game_data import data
from art import vs
from art import logo
from replit import clear
print(logo)


def generate_random():
  rand_num = random.randint(0,len(data)-1)
  return rand_num


def comparator(letter,random_num1,random_num2):
  if(letter=="A" and data[random_num1]['follower_count']>data[random_num2]['follower_count']):
    return True
  if(letter=="A" and data[random_num1]['follower_count']<data[random_num2]['follower_count']):
    return False
  if(letter=="B" and data[random_num1]['follower_count']<data[random_num2]['follower_count']):
    return True
  if(letter=="B" and data[random_num1]['follower_count']>data[random_num2]['follower_count']):
    return False

    
def compare_prompt(letter,rand_num):
  print(f"Compare {letter}: {data[rand_num]['name']}, {data[rand_num]['description']} from {data[rand_num]['country']}")


def return_more_followers(random_num1,random_num2):
  if(data[random_num1]['follower_count']>data[random_num2]['follower_count']):
    return random_num1
  else:
    return random_num2


def return_less_followers(random_num1,random_num2):
  if(data[random_num1]['follower_count']>data[random_num2]['follower_count']):
    return random_num2
  else:
    return random_num1
    

def input_response():
  while(True):
    response = input()
    if(response.upper() == "A" or response.upper() =="B"):
      break
    else:
      print("Invalid response. Type A or B.")
  return response


user_points = 0  
rand_num1 = generate_random()

while(True):
  while(True):
    rand_num2 = generate_random()
    if rand_num2!=rand_num1:
      break
  compare_prompt("A",rand_num1)
  print(vs)
  compare_prompt("B",rand_num2)
  
  response = input_response()
  
  if(comparator(response,rand_num1,rand_num2)==False):
    print("You lost.")
    print(f"Score: {user_points}")
    break
  user_points+=1
  clear()
  print(f"Score: {user_points}")
  temp = return_less_followers(rand_num1,rand_num2)
  rand_num1=return_more_followers(rand_num1,rand_num2)
  
  while(True):
    rand_num2 = generate_random()
    if rand_num2!=rand_num1 and rand_num2!=temp:
      break
