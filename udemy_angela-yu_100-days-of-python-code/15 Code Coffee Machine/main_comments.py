
# VARIABLES in Global Scope
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# FUNCTIONS

# Check resources (requirement 4)
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""

    """E.g. if Latte requires 200ml water but there 
    is only 100ml left in the machine. 
    It should not continue to make the drink but print 
    'Sorry there is not enough water'"""
    is_enough = True
    for item in order_ingredients:
        # If any of the order ingredients is greater than the resources
        if order_ingredients[item]>= resources[item]:
            print (f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough

# Process coins (Requirment 5)
def process_coins():
    """ Returns the total calculated from coins inserted."""

    """Remember that quarters = $0.25, dimes = $0.10, 
    nickles = $0.05, pennies = $0.01. 
    Calculate the monetary value of the coins inserted. 
    E.g. 1 quarter, 2 dimes, 1 nickel, 2
    pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52"""

    print("Please insert coins.")
    total = int(input("How many quearters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

# Check transaction successful (Requirement 6)
    # Check that the user has inserted enough money to purchase the drink they selected
def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change =round (money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost # Check global variable
        return True
    else:
        print("​Sorry that's not enough money. Money refunded.")
        return False

# Make Coffe (Requirement 7)
def make_coffee(drink_name,order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")
        

# ----------------

is_on = True
while is_on:
    # Prompt user (Requirement 1)
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    
    # If input is "off" - turn off the Coffe Machine (Requirement 2)
    if choice == "off":
        is_on = False
    
    # If input is "report"  to print report (requirement 3)
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffe: {resources['coffee']}g")
        print(f"Money: ${profit}")
    
    # If input is "espresso/latte/cappuccino" entering drink name
    else:
        drink = MENU[choice] # ingredients & cost for each drink

        # Check resources (requirement 4)
        if is_resource_sufficient(drink["ingredients"]):

            # Process coins (Requirement 5)
            payment = process_coins()

            # Check if the transaction is succesful (Requirement 6)
            if is_transaction_successful(payment, drink["cost"]):
                # Make coffee (Requirement 7)
                make_coffee(choice,drink["ingredients"])
