import random

from art import vs, logo
from game_data import data


def get_account():
    return random.choice(data)


def format_data(account):
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, account_a_follower, account_b_follower):
    if account_a_follower > account_b_follower:
        return guess == 'a'
    elif account_a_follower < account_b_follower:
        return guess == 'b'


def game():
    print(logo)
    account_a = get_account()
    account_b = get_account()
    should_continue = True
    score = 0
    while account_a == account_b:
        account_b = get_account()

    while should_continue:
        account_a = account_b
        account_b = get_account()
        print(f"Compare A:{format_data(account_a)}")
        print(vs)
        print(f"Compare B:{format_data(account_b)}")
        guess = input(f"Who has more followers? Type 'A' or 'B': ").lower()
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        is_score = check_answer(guess, a_followers, b_followers)
        if is_score:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
