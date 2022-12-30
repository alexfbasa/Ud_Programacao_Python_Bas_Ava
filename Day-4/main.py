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

get_user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
choices = [rock, paper, scissors]
size_choices = len(choices)
computer_choice = random.randint(0, size_choices - 1)
print(f"Your bet {choices[get_user_choice]}")
print(get_user_choice)
print(f"Computer chose: {choices[computer_choice]}")
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
