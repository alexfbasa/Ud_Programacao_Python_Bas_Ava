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

profit = 0
is_machine_on = True


def format_report(machine_resource):
    water = machine_resource['water']
    milk = machine_resource['milk']
    coffee = machine_resource['coffee']
    return f"Water: {water}ml.\n" \
           f"Milk: {milk}ml.\n" \
           f"Coffee: {coffee}ml\n" \
           f"Profit: ${profit}"


def is_sufficient_resource(resource_available, selected_drink):
    for ingredient, required_amount in selected_drink['ingredients'].items():
        if resource_available[ingredient] < required_amount:
            print(f"Sorry, not enough {ingredient}.")
            return False
        return True


def get_coins():
    print('Please insert coins.')
    payment = float(input('How many quarters? ')) * 0.25
    payment += float(input('How many dimes? ')) * 0.1
    payment += float(input('How many nickles? ')) * 0.05
    payment += float(input('How many pennies? ')) * 0.01
    return payment


def make_payment(drink_price, payment):
    """Get a drink and a payment and returns whether payment is enough."""
    if payment >= drink_price['cost']:
        change = payment - drink_price['cost']
        global profit
        print(f"Here is ${change:.2f} in change.")
        profit += drink_price['cost']
        return True
    else:
        print(f"Sorry, there is not enough coins.")
        print(f"Here is your refund ${payment}.")
        return False


def make_drink(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. ENJOY :)")


while is_machine_on:
    choice = input(f"What would you like? (espresso/latte/cappuccino): 	").lower()
    if choice == 'off':
        print("Turning off.")
        is_machine_on = False
    elif choice == "report":
        print(format_report(resources))
    else:
        drink = MENU[choice]
        if is_sufficient_resource(resources, drink):
            user_coins = get_coins()
            if make_payment(drink, user_coins):
                make_drink(choice, drink['ingredients'])
