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
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f'Sorry. There is not enough {item}.')
            return False
    return True


def process_coins():
    print('Please insert the coins.')
    total = int(input('Hom many quarters? ')) * 0.25
    total += int(input('Hom many dimes? ')) * 0.1
    total += int(input('Hom many nickles? ')) * 0.05
    total += int(input('Hom many pennies? ')) * 0.01
    return total


def is_payment_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f'Here is ${change} in change.')
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


print(logo)
is_on = True
profit = 0
while is_on:

    user_choice = input(f"What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        is_on = False
        print('Turning coffee machine down.')
    elif user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}.")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
        else:
            print('There is no ingredients')
            is_on = False
