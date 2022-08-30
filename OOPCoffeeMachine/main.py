from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
should_continue = True
while should_continue:
    order = input("What would you like? (" + menu.get_items() + "): ")
    if order == "off":
        should_continue = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(order)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)









