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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def coffee_machine():
    while True:
        user_answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_answer == "espresso":
            if check_resources(50, 18, 0):
                if check_coins(1.50, 50, 18,0):
                    print("Here is your Espresso. Enjoy!")
        elif user_answer == "latte":
            if check_resources(200, 24, 150):
                if check_coins(2.5, 200, 24, 150):
                    print("Here is your Latte. Enjoy!")
        elif user_answer == "cappuccino":
            if check_resources(250, 24, 100):
                if check_coins(3.0, 250, 24, 100):
                    print("Here is your Cappuccino. Enjoy!")
        elif user_answer == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffe']}g")
            print(f"Money: ${resources['money']}")
        elif user_answer == "off":
            return False
        else:
            print("Please enter valid syntax")
            coffee_machine()


def check_resources(check_water, check_milk, check_coffe):
    water = resources["water"]
    milk = resources["milk"]
    coffe = resources["coffee"]
    if check_water > water:
        print("Sorry, there is not enough water")
        return False
    elif check_coffe > coffe:
        print("Sorry, there is not enough coffee")
        return False
    elif check_milk > milk:
        print("Sorry there is not enough milk")
        return False
    else:
        return True


def process_coins():
    print("Please insert coins. ")
    quarters = int(input("How many quarters?: $"))
    dimes = int(input("How many dimes?: $"))
    nickles = int(input("How many nickles?: $"))
    pennies = int(input("How many pennies?: $"))
    total = round(quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01, 2)
    return total


def check_coins(exchange, water1, coffe1, milk1):
    resources["water"] -= water1
    resources["coffee"] -= coffe1
    resources["milk"] -= milk1
    resources["money"] += exchange
    coin = process_coins()
    if coin - exchange < 0:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif coin - exchange == 0:
        return True
    else:
        print(f"Here is ${round(coin - exchange, 2)} in change.")
        return True


coffee_machine()
