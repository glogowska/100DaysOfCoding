MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MONEY_EARNED = 0


def report_print():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")


def use_resources(coffee_type):
    resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']


def check_resources(coffee_type):
    if resources['water'] - MENU[coffee_type]['ingredients']['water'] < 0 or resources['milk'] - \
            MENU[coffee_type]['ingredients']['milk'] < 0 or resources['coffee'] - \
            MENU[coffee_type]['ingredients']['coffee'] < 0:
        print("Not enough ingredients:")
        if resources['water'] - MENU[coffee_type]['ingredients']['water'] < 0:
            print("Not enough water.")
        if resources['milk'] - MENU[coffee_type]['ingredients']['milk'] < 0:
            print("Not enough milk.")
        if resources['coffee'] - MENU[coffee_type]['ingredients']['coffee'] < 0:
            print("Not enough coffee.")
        return False
    else:
        return True


def processing_coins():
    print("Insert coins.")
    quarters = int(input("How many quarters?: $"))
    dimes = int(input("How many dimes: $"))
    nickles = int(input("How many nickles: $"))
    pennies = int(input("How many pennies: $"))

    payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return payment


def enough_money(payment, coffee_type):
    if payment == MENU[coffee_type]['cost']:
        adding_money(payment)
        return True
    elif payment >= MENU[coffee_type]['cost']:
        refund = payment - MENU[coffee_type]['cost']
        print(f"Refunding ${refund}.")
        return True
    else:
        print("Sorry, there is not enough money. Money refunded.")
        return False


def adding_money(money):
    global MONEY_EARNED
    MONEY_EARNED += money


def giving_coffee(coffee_type):
    print(f"Here is your {coffee_type}! Enjoy :)")


def coffee_machine():
    while True:
        response = input("What would you like? (espresso/latte/cappuccino):")
        if response == "off":
            print("Machine is off.")
            break
        elif response == "espresso" or response == "latte" or response == "cappuccino":
            if check_resources(response):
                coins = processing_coins()
                if enough_money(coins, response):
                    use_resources(response)
                    giving_coffee(response)
                    coffee_machine()
                else:
                    coffee_machine()
            else:
                coffee_machine()
        elif response == "report":
            report_print()
        # Assuming that the user cannot pick anything other than these three types of coffee, report option
        # and 'off' option


coffee_machine()