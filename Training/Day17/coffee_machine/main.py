from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    drinks = menu.get_items()
    choice = input(f"What would you like? ({drinks}):").lower()
    if choice == "off":
        print("Turning Coffee machine OFF.")
        is_on = False
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

# . Prompt user by asking “What would you like? (espresso/latte/cappuccino/):”


