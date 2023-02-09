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
}


def report(machine_resources):
    head_message = "The current machine resources is:"
    water = machine_resources['water']
    milk = machine_resources['water']
    coffee = machine_resources['water']
    return f"{head_message} \nWater = {water}ml\nMilk = {milk}ml\nCoffee = {coffee}g"


def get_drink_name():
    drinks = []
    for v in MENU:
        drink = v.title()
        drinks.append(drink)
    return drinks


def sufficient_resources(drink_ingredients, machine_resources):
    if drink_ingredients > machine_resources:
        return False


is_machine_on = True

while is_machine_on:
    my_drink = get_drink_name()
    get_user_choice = input(f'Select your drink {my_drink}: ')
    if get_user_choice == 'report':
        print(report(resources))
    elif get_user_choice == 'off':
        print('Shutting the machine down.')
        is_machine_on = False
    elif get_user_choice in my_drink:
        pass
