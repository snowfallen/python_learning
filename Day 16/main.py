from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
new_coffe = MenuItem("Moccacino", 100, 150, 30, 3.5)

print(menu.find_drink(new_coffe))

def make_coffee():
    while True:
        user_answer = input(f"What would you like? {menu.get_items()}: ").lower()
        if user_answer == "report":
            coffe_maker.report()
            money_machine.report()
        elif user_answer == "off":
            return False
        else:
            drink = menu.find_drink(user_answer)
            if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)


# make_coffee()
