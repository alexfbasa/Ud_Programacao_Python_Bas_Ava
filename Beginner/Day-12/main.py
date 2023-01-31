import random

from art import logo

print(logo)
print('Welcome to the Number Guessing Game!')

LEVEL_EASY = 10
LEVEL_HARD = 5

game_is_on = True


def game_level():
    get_difficulty_level = input(f"Choose a difficulty. Type 'easy' or 'hard:'")
    if get_difficulty_level.lower() == 'hard':
        return LEVEL_HARD
    elif get_difficulty_level.lower() == 'easy':
        return LEVEL_EASY
    else:
        print('Level not found:')


def compare_answer(guess_number, secret_number, turns):
    if guess_number > secret_number:
        print('Too high.')
        return turns - 1
    elif guess_number < secret_number:
        print('Too low.')
        return turns - 1
    else:
        print('You guessed right. Congratulations.')


def game():
    turns = game_level()
    print(f"I'm thinking of a number between 1 and 100.")
    number_randon = random.randint(1, 100)
    print(f"Pssst, the correct answer is {number_randon}")
    guess = 0

    while guess != number_randon:
        guess = int(input('Make a guess.'))
        compare_answer(guess, number_randon, turns)
        print(f'You have more {turns} chances.')
        if turns == 0:
            print('The game is over')
            return
