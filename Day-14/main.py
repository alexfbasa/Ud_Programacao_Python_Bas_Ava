# TODO 1 - Show game logo:
import random

from art import logo, vs
from game_data import data

print(logo)


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    user_guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()


# Compare A: LeBron James, a Basketball player, from United States.
# TODO 2 - Show the comparison A
# TODO 3 - Show VS Logo
# TODO 4 - Show comparison B
# TODO 5 - Make the question about comparison
