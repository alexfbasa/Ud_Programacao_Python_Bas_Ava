import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_images = [rock, paper, scissors]
choice_size = len(choice_images)
is_game_on = True


def get_computer_choice():
    computer_choice = random.randint(0, choice_size - 1)
    return computer_choice


def get_user_choice():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
    return user_choice


def count_score():
    score = 0
    return score + 1


while is_game_on:
    print("Welcome to ROCK - PAPER - SCISSOR -- GAME ")
    user = get_user_choice()
    print("Player ")
    print(choice_images[user])
    print("--------------VS--------------")
    computer = get_computer_choice()
    print("Computer ")
    print(choice_images[computer])
    if computer == user:
        print("You've got a DRAW. ")
    else:
        if computer > user:
            print("You lose. ")
        else:
            print("You win. ")
