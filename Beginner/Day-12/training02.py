import random

from art import logo

print(logo)
EASY_MODE = 5
HARD_MODE = 10


def get_game_level():
    get_user_choice = input("Choose your game mode: Type 'easy' or 'hard'")
    try:
        if get_user_choice.lower() == 'easy':
            return EASY_MODE
        elif get_user_choice.lower() == 'hard':
            return HARD_MODE
        else:
            print('Game mode not valid.')
    except:
        print('You wrote an invalid game mode.')


def track_guesses(user_guess, correct_answer, turn):
    if user_guess > correct_answer:
        print('Too high.')
        return turn - 1
    elif user_guess < correct_answer:
        print('Too low.')
        return turn - 1
    else:
        print(f'You guessed right. Congratulations. The answer was {correct_answer}')


def game():
    random_number = random.randint(1, 100)
    print(f"DEBUG number secret is {random_number}")
    print('Welcome to the Number Guessing Game!')
    print(f"I'm thinking of a number between 1 to 100.")
    turns = get_game_level()
    guess = 0
    while guess != random_number:
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess = int(input('Make a guess. ;) '))
        turns = track_guesses(guess, random_number, turns)
        if turns == 0:
            print('Game over.')
            return
        elif guess != random_number:
            print('Guess again. ')


game()
