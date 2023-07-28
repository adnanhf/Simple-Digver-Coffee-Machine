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


def is_resource_sufficient(order_ingredients):
    """
    This function created 3rd
    Returns True when an order can be made. Returns
    False if ingredients are insufficient.
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    This function created 4th
    Returns the total calculated from coins inserted.
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """
    This function created 5th
    Return True when the payment is accepted,
    or False if money is insufficient.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """
    This function created 6th
    Deduct the required ingredients from the resources.
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


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

        else:
            drink = MENU[choice]
            # TODO: 4. Check whether resources sufficient or insufficient.
            if is_resource_sufficient(drink["ingredients"]):

                # TODO: 5. Process coins.
                payment = process_coins()
                
                # TODO: 6. Check transaction succeeded or failed.
                if is_transaction_successful(payment, drink["cost"]):
                    # TODO: 7. Make the coffee if transaction succeed.
                    make_coffee(choice, drink["ingredients"])
    
