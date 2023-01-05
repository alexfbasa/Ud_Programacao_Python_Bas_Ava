import random
from game_data import data
from art import logo, vs
from replit import clear


def format_account(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, follower_a, follower_b):
    """Check user guess against followers printed"""
    if follower_a > follower_b:
        return guess == 'a'
    else:
        return guess == 'b'


score = 0
should_game_continue = True
account_b = random.choice(data)
print(logo)
while should_game_continue:
    account_a = account_b
    account_b = random.choice(data)
    # Replaced if for while the will replace until no longer equal.
    while account_a == account_b:
        account_b = random.choice(data)
    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']
    print(f"Compare A: {format_account(account_a)}.")
    print(vs)
    print(f"Against B: {format_account(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    is_correct = check_answer(guess, followers_a, followers_b)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")

    else:
        should_game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
