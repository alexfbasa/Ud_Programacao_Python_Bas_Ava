import random

from art import logo

EASY_MODE = 10
HARD_MODE = 5
LIVES = 0
print(logo)


def difficulty():
    get_user_level = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
    if get_user_level == 'easy':
        return EASY_MODE
    elif get_user_level == 'hard':
        return HARD_MODE
    else:
        print("Invalid input. Choosing easy mode by default.")
        return EASY_MODE


is_game_on = True

print("Welcome to the Number Guessing Game! ")
print("I am thking of a number between 1 and 100. ")
level = difficulty()
while is_game_on:
    secret_number = random.randint(1, 101)
    if level > 0:
        get_user_shot = int(input("Guess a number:"))
        if get_user_shot > secret_number:
            print('Too high:')
            level -= 1
        elif get_user_shot < secret_number:
            print('Too low:')
            level -= 1
        else:
            print(f"Congratulations, is was thinking {secret_number}.")
            is_game_on = False
    else:
        is_game_on = False


