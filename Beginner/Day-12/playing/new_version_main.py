import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def get_difficulty_level() -> int:
    """Asks the user to choose a difficulty level and returns the number of attempts."""
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard'").lower()
        if level == 'easy':
            return EASY_ATTEMPTS
        elif level == 'hard':
            return HARD_ATTEMPTS
        else:
            print("Invalid input. Please choose 'easy' or 'hard'.")


def play_game() -> None:
    """Runs the number guessing game."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(0, 100)
    attempts = get_difficulty_level()
    print(f"You have {attempts} attempts remaining to guess the number.")
    while attempts > 0:
        guess = int(input("make a guess: "))
        if guess == answer:
            print(f"You got it! The answer was {answer}.")
            return
        elif guess > answer:
            print("Too high.")
        else:
            print("Too low.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.")

    print(f"Sorry, you ran out of attempts. The answer was {answer}.")

play_game()