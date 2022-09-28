import pandas

# Creating a dictionary from the csv file:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in data.iterrows():
    nato_alpa = {row.letter: row.code for (index, row) in data.iterrows()}

# print(nato_alpa)

# Creating a list of the phonetic code words from a word that the user inputs:
user_input = (input("Enter a word: ")).upper()
user_input = list(user_input)
user_list = [nato_alpa[letter] for letter in user_input]
print(user_list)
