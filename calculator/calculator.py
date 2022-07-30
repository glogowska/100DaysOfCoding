from replit import clear
from art import logo

print(logo)
def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  op = input("Type in a symbol of one of the operations above: ")
  
  num2 = float(input("What's the second number?: "))
  
  function = operations[op]
  
  answer = function(num1,num2)
    
  
  print(f"{num1} {op} {num2} = {answer}")
  
  while True:
    continuation = input("Type 'y' to continue and 'n' to start a new calculation: ")
  
    if continuation == "n":
      clear()
      calculator()
  
    for symbol in operations:
      print(symbol)
    op2 = input("Type in a symbol of one of the operations above: ")
  
    num3 = float(input("Pick the next number: "))
  
    function2 = operations[op2]
    answer2 = function2(answer,num3)
    
    print(f"{answer} {op2} {num3} = {answer2}")
    answer = answer2

calculator()