from art import logo

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
    "coffee": 1000,
}

profit = 0


def get_drink_names():
    drinks = []
    for drink in MENU:
        drinks.append(drink)
    return drinks


def report(machine_resources):
    water = machine_resources['water']
    milk = machine_resources['milk']
    coffee = machine_resources['coffee']
    return f"Water : {water}ml.\nMilk : {milk}ml.\nCoffee : {coffee}g.\nMoney: {profit}"


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        #  drink['ingredients'][item] > resources[item]
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def get_payment():
    print('Please insert coins.')
    total = 0
    try:
        total = int(input('how many quarters?: ')) * 0.25
        total += int(input('how many dimes?: ')) * 0.10
        total += int(input('how many nickles?: ')) * 0.5
        total += int(input('how many pennies?: ')) * 0.01
    except:
        print('No coins inserted.')
    return total


def check_transaction_successful(user_payment, drink_cost):
    if user_payment >= drink_cost:
        change = round(user_payment - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


machine_is_on = True

while machine_is_on:
    get_user_command = input(f"What would you like? {get_drink_names()}:").lower()
    if get_user_command == 'report':
        print(report(resources))
    elif get_user_command == 'off':
        machine_is_on = False
        print('Turning Coffee Machine down.')

    elif get_user_command in get_drink_names():
        drink = MENU[get_user_command]
        if is_resource_sufficient(drink['ingredients']):
            payment = get_payment()
            if check_transaction_successful(payment, drink['cost']):
                make_drink(get_user_command, drink['ingredients'])
    else:
        print('Invalid input.')
        pass
