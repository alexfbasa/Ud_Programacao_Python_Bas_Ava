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
        if order_ingredients[item] > resources[item]:
            print(f'Sorry. There is not enough {item}.')
            return False
    return True


def make_payment():
    print('Please insert the coins.')
    total = int(input('Hom many quarters? ')) * 0.25
    total += int(input('Hom many dimes? ')) * 0.10
    total += int(input('Hom many nickles? ')) * 0.5
    total += int(input('Hom many pennies? ')) * 0.1
    return total


def check_payment_enough(payment, drink):
    global profit
    if payment >= MENU[drink]:
        profit += payment
        return True
    else:
        print("Payment was not enough")
        return False


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
        drink = MENU[get_user_choice]['ingredients']
        if is_resources_sufficient(drink):
            print("Checking the coins.")
            get_payment = make_payment()
            if check_payment_enough(get_payment, get_user_choice):
                print("Here is your drink, enjoy :) ")
        else:
            print("Ainda ta dando bomm")
