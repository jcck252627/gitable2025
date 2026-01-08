from importlib.resources import is_resource

from botocore.compat import total_seconds
from twisted.python.compat import items

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


def resource_sufficient_check(ingredients):
    for items in ingredients:
        if ingredients[items] >= resources[items]:
            print(f"Sorry, there is not enough {items}. ")
            return False
    return True

def calculate_coins():
    """
    return calculated coin total to buy the drink so the order can be made
    """
    print("Please insert coins...")
    total= int(input("Enter the quarters you inserted:  ")) * 0.25
    total += int(input("Enter the dimes you inserted:  ")) * 0.1
    total += int(input("Enter the nickles you inserted:  ")) * 0.05
    total += int(input("Enter the pennies you inserted:  ")) *0.01
    return total

"""
return true if enough money to buy drink , false if not
"""
def is_money_enough(money_in, cost):
    if money_in >= cost:
        change = round(money_in - cost, 2)
        print(f"Here is ${change} in change returned to you...........")
        global profit
        profit += cost
        return True
    else:
        print("Sorry ! ... not enough money is inserted, the money will be refunded")
        return False

"""
when making coffee , deduct the resouces
"""
def deduct_resources(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")



machine_is_on = True

while machine_is_on:
    customer_choice =input("What would you like? (espresso/latte/cappuccino):  ")
    if customer_choice == "off":
        machine_is_on = False
    elif customer_choice =="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[customer_choice]
        print(drink)
        if resource_sufficient_check(drink["ingredients"]):
            payment= calculate_coins()
            if is_money_enough(payment, drink["cost"]):
                deduct_resources(customer_choice, drink["ingredients"])


# v106 at 24:50 .... to start working on resources deductions

print("Machine is in maintenance mode now ....")
