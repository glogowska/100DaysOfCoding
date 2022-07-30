from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

bidding_dictionary = {}

def add_value(name_input,dollars):
  bidding_dictionary[name_input] = dollars

response = "yes"
while response =="yes":
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  add_value(name,bid)
  response = input("Do you want to bid again? Type 'yes' or 'no'. ")
  clear()

def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_name = ""
  for names in bidding_record:
    if bidding_record[names] > highest_bid:
      highest_bid = bidding_record[names]
      highest_name = names
    
  print(f"The highest bid was {highest_name}'s and it was ${highest_bid}.")

find_highest_bidder(bidding_dictionary)
