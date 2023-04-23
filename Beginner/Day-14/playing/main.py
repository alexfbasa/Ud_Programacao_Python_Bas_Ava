import random

from replit import clear

from game_data import data
from art import logo, vs



def get_random_account():
    """Check game_data and returns one random account."""
    return random.choice(data)


def format_data(account: dict) -> str:
    name: str = account['name']
    description: str = account['description']
    country: str = account['country']
    return f"{name}, {description}, from {country}."


def check_answer(user_guess, account_a, account_b):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if account_a > account_b:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

def play_game():
    is_game_on = True
    score = 0

    account_a = get_random_account()
    account_b = get_random_account()

    while is_game_on:
        print(logo)
        print(f"Compare A: {format_data(account_a)}")
        if account_a == account_b:
            account_b = get_random_account()
        print(vs)
        print(f"Against B: {format_data(account_b)}")
        print(f"You currently score {score}")
        guess = input("Who has more followers? Type 'A' or 'B' ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        answer = check_answer(guess, a_follower_count, b_follower_count)
        if answer:
            account_a = account_b
            score += 1
        else:
            print("Wrong answer. You lose.")
            print(f"Account A has {account_a['follower_count']} and Account B has {account_b['follower_count']}")
            if input("Do you want to play again? Type 'yes' or 'no' ").lower() == 'yes':
                clear()
                play_game()
            else:
                print(f"You currently score {score}. Game over. ")
                is_game_on = False

play_game()