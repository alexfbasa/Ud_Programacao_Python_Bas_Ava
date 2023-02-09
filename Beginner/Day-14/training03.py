import random

from art import vs
from game_data import data


def choice_account():
    return random.choice(data)


def format_account(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, {country}."


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    elif a_followers < b_followers:
        return guess == 'b'


def game():
    score = 0
    should_continue = True
    account_a = choice_account()
    account_b = choice_account()
    while account_a == account_b:
        account_b = choice_account()

    while should_continue:
        account_a = account_b
        account_b = choice_account()
        print(f"Compare A:{format_account(account_a)}")
        print(vs)
        print(f"Against B:{format_account(account_b)}")
        get_user_guess = input("Who has more followers? 'A' or 'B':").lower()
        account_a_followers = account_a['follower_count']
        account_b_followers = account_b['follower_count']
        is_correct = check_answer(get_user_guess, account_a_followers, account_b_followers)
        if is_correct:
            score += 1
        else:
            print('You got wrong.')
            print(f'Your score was {score}. Game Over.')
            print(f'Game Over.')
            should_continue = False


game()
