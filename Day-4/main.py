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
game_images = [rock, paper, scissors]
get_user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))

if get_user_choice <= 3 or get_user_choice < 0:
    print('You typed an invalid number. You lose')
else:
    size_choices = len(game_images)
    computer_choice = random.randint(0, size_choices)
    print(f"Your bet {game_images[get_user_choice]}")
    print(get_user_choice)
    print(f"Computer chose: {game_images[computer_choice]}")
    print(computer_choice)
    if get_user_choice == 0 and computer_choice == 2:
        print('You win.')
    elif computer_choice == 0 and get_user_choice == 2:
        print('You lose.')
    elif get_user_choice > computer_choice:
        print('You win.')
    elif computer_choice > get_user_choice:
        print('You lose.')
    elif computer_choice == get_user_choice:
        print(f"It's a draw.")
