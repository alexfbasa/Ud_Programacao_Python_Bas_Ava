import random
from replit import clear
from game_data import data
from art import logo, vs


def get_random_account() -> dict:
    """Returns a randomly chosen account from the data."""
    return random.choice(data)


def format_account(account: dict) -> str:
    """Returns a formatted string representation of an account."""
    return f"{account['name']}, {account['description']}, from {account['country']}."


def get_user_guess() -> str:
    """Gets the user's guess and ensures that it is valid."""
    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess in ['a', 'b']:
            return guess
        else:
            print("Invalid input. Please try again.")


def check_answer(guess: str, a_followers: int, b_followers: int) -> bool:
    """Checks if the user's guess is correct and returns True or False."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'


def play_game() -> None:
    """Plays a game of Higher Lower."""
    score = 0

    account_a = get_random_account()
    account_b = get_random_account()

    while True:
        clear()
        print(logo)
        print(f"Compare A: {format_account(account_a)}")
        print(vs)
        print(f"Against B: {format_account(account_b)}")
        print(f"Your current score: {score}")

        user_guess = get_user_guess()
        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]
        if check_answer(user_guess, a_followers, b_followers):
            score += 1
            print("You got it right!")
            account_a = account_b
            account_b = get_random_account()
        else:
            print("Sorry, that's wrong.")
            print(f"Final score: {score}")
            play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if play_again == 'yes':
                score = 0
                account_a = get_random_account()
                account_b = get_random_account()
            else:
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    play_game()
