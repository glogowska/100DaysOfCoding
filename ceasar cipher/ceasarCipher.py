from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while 1:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift>26:
    shift = shift%26
  
  def ceasar(before_text,shift_amount,direction_ceasar):
    after_text = ""
    for letter in before_text:
      if letter in alphabet:
        number = alphabet.index(letter)
        if direction_ceasar == "encode":  
          after_text += alphabet[number + shift_amount]
          
        elif direction_ceasar == "decode":
          after_text += alphabet[number - shift_amount]
      else:
        after_text += letter
        
    print(f"The {direction_ceasar}d test is: " + after_text)
  
  
  ceasar(text,shift,direction)

  response = input("Type 'yes' if you want to start over or 'no' if you want to exit: ")
  if response == "no":
    print("Goodbye!")
    break
  elif response != "yes":
    print("Wrong response! Goodbye")
    break

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

