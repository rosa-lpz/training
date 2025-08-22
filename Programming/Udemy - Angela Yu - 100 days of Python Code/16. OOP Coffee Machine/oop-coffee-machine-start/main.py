from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 1. PRINT REPORT

# Object = Class ()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()



# Object.method - Print Report (Req 1)
# money_machine.report()
# coffee_maker.report()

# Variables
is_on = True

while is_on:
    # All menu names available will be stored in "options" variable
    options = menu.get_items()

    # Prompt “​What would you like? (espresso/latte/cappuccino):
    choice = input(f"What would you like ? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # 2. CHECK RESOURCES
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




# 1. 

#while True:
#   choice = input ("What would you like? (espresso/latte/cappuccino):")