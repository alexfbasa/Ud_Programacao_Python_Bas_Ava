from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

print(logo)

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True

while machine_is_on:
    get_user_command = input(f"What would you like? ({menu.get_items()}): ")
    if get_user_command == 'off':
        print(f"Turning the Coffee Machine DOWN!")
        machine_is_on = False
    elif get_user_command == 'report':
        coffee_maker.report()
        money_machine.report()
    elif get_user_command in menu.get_items():
        drink = menu.find_drink(get_user_command)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
