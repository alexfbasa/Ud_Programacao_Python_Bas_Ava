from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()


def get_drinks():
    is_machine_on = True
    while is_machine_on:
        options = menu.get_items()
        get_user_choice = input(f"What would you like? ({options}): ").lower()
        if get_user_choice == "off":
            print("Coffee Machine OFF-LINE! ")
            is_machine_on = False
        elif get_user_choice == 'report':
            coffe_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(get_user_choice)
            print(drink)
            if coffe_maker.is_resource_sufficient(drink):
                payment_enough = money_machine.make_payment(drink.cost)
                if payment_enough:
                    coffe_maker.make_coffee(drink)


get_drinks()
