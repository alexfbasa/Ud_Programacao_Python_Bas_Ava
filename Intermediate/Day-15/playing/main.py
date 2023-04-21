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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resource: dict) -> str:
    return f"Water = {resource['water']};\n" \
           f"Milk = {resource['milk']}; \n" \
           f"Coffee = {resource['coffee']};\n" \
           f"Profit {profit}"


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry. There is not enough {item}.')
            return False
    return True


def make_payment():
    """Returns the total of coins inserted. """
    print('Please insert the coins.')
    total = int(input('Hom many quarters? ')) * 0.25
    total += int(input('Hom many dimes? ')) * 0.10
    total += int(input('Hom many nickles? ')) * 0.5
    total += int(input('Hom many pennies? ')) * 0.1
    return total


def check_payment_enough(money_received, drink_cost):
    """Return True when the payment accepted, or False if moneys is insufficient."""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change ${change}")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here your {drink_name} enjoy: ")


is_machine_on = True

while is_machine_on:
    print(logo)
    get_user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if get_user_choice == 'report':
        print(print_report(resources))
    elif get_user_choice == "off":
        print("Coffee Machine off.")
        is_machine_on = False
    else:
        drink = MENU[get_user_choice]
        if is_resources_sufficient(drink['ingredients']):
            print("Checking the coins.")
            get_payment = make_payment()
            if check_payment_enough(get_payment, drink['cost']):
                make_coffe(get_user_choice, drink['ingredients'])
