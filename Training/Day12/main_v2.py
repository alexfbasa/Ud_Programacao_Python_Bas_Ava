import random

from art import logo

EASY_MODE = 10
HARD_MODE = 5
print(logo)


def check_answer(guess, answer, turns):
    if guess > answer:
        print('Too high.')
        return turns - 1
    elif guess < answer:
        print('Too low.')
        return turns - 1
    elif guess == answer:
        print(f"You've got it, the answer is {answer}.")


def set_difficulty():
    get_user_level = input(f"Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if get_user_level == 'easy':
        return EASY_MODE
    elif get_user_level == 'hard':
        return HARD_MODE
    else:
        print("Invalid input. Choosing easy mode by default.")
        return EASY_MODE


is_game_on = True

print("Welcome to the Number Guessing Game! ")
print("I am thinking of a number between 1 and 100. ")
turns = set_difficulty()
answer = random.randint(1, 100)
guess = 0

while guess != answer:
    print(f"You have {turns} turns. ")
    guess = int(input('Make a guess:: '))
    turns = check_answer(guess, answer, turns)
