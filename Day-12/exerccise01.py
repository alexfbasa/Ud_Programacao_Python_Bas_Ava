# Number Guessing Game Objectives:

# TODO 01 - Include an ASCII art logo - Done
from art import logo
import random

print(logo)

# TODO 04 - Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
HARD_MODE = 5
EASY_MODE = 10


def select_difficulty_level():
    choose_leve = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if choose_leve == 'hard':
        return HARD_MODE
    elif choose_leve == 'easy':
        return EASY_MODE
    else:
        print('Mode not found! ')


# TODO 03 - Check user's guess against actual answer. Print "Too high." or "Too low."
#  depending on the user's answer. - Done


def check_answer(guess, answer, turns):
    """Check answers against guess. Return number of turns remaining."""
    if guess > answer:
        print('Too high.')
        return turns - 1
    elif guess < answer:
        print('Too low.')
        return turns - 1
    else:
        print(f'You got it! The answer is {answer}.')


def game():
    print('Welcome to the Number Guessing Game!')
    print(f"I'm thinking of a number between 1 and 100.")
    random_answer = random.randint(0, 100)
    print(f"Debug, the correct answer is {random_answer}")
    # TODO 02 - Allow the player to submit a guess for a number between 1 and 100 - Done
    # TODO 05 - Track the number of turns remaining. Done
    turns = select_difficulty_level()
    guess = 0

    while guess != random_answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess = int(input(f"Make a Guess a number between 1 and 100? "))
        turns = check_answer(guess, random_answer, turns)
        if turns == 0:
            print('The game is over')
            return


# If they got the answer correct, show the actual answer to the player.
# If they run out of turns, provide feedback to the player.


game()
