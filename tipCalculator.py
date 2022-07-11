print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What procentage bill would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

divided_bill = round((total_bill*(1+tip/100))/people, 2)

print(f"Each person should pay: ${divided_bill}")