#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
names = []
clear_names = []
with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    clear_name = name.strip("\n")
    clear_names.append(clear_name)
print(clear_names)
with open("./Input/Letters/starting_letter.txt") as letter:
    starting_text = letter.read()
for n in clear_names:
    print(n)
    new_letter = open(f"./Output/ReadyToSend/letter_for_{n}", mode="w")
    new_text = starting_text.replace("[name]", n)
    new_letter.write(new_text)
# print(names)
