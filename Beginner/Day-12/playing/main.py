from random import randint
from art import logo

EASY = 10
HARD = 5


def difficulty():
    get_difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if get_difficulty_level == 'easy':
        return EASY
    elif get_difficulty_level == 'hard':
        return HARD
    else:
        return "You typed a wrong difficulty mode. "


def check_answer(guessed_number, number, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guessed_number > number:
        print("Too high. ")
        return turns - 1
    elif guessed_number < number:
        print("Too low. ")
        return turns - 1
    else:
        print(f"You got it! The answer was {guessed_number}.")


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print('I am thinking of a number between 1 and 100.')
    answer = randint(1, 100)
    print(answer)
    user_lives = difficulty()
    print(f"You have {user_lives} attempts remaining to guess the number.")
    guess = 0

    while guess != answer:
        guess = int(input('Make a guess.'))
        turns = check_answer(guess, answer, user_lives)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


play_game()
