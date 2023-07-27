# This variable created 1st
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


def main():
    # This function created 2nd
    is_on = True
    while is_on:
        # TODO: 1. Prompt the user by asking “What would you like? (espresso/latte/cappuccino):”
        choice = input("What would you like? (espresso/latte/cappuccino): ")
    
        # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
        if choice == "off":
            is_on = False
            
        # TODO: 3. Print report (resources and money).
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
            
    # TODO: 4. Check resources sufficient or insufficient.
    # TODO: 5. Process coins.
    # TODO: 6. Check transaction succeed or failed.
