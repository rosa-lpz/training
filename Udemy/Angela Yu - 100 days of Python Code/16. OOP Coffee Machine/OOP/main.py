from menu import Menu, MenuItem 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1. PRINT REPORT
money_machine = MoneyMachine()
coffee_maker= CoffeeMaker()
menu = Menu()


money_machine.report()
coffee_maker.report()


# 2. CHECK RESOURCES
# coffee_maker.is_resource_sufficient()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input (f"What would you like? ({options}):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        # If the choice is
        drink = menu.find_drink(choice)
        
        # check if the resource is sufficient
        if coffee_maker.is_resource_sufficient(drink):
            print(money_machine.make_payment(drink.cost))