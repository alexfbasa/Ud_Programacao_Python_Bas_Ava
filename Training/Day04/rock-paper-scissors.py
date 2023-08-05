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

# Write your code below this line 👇

# Store the images in a dictionary for easier access
images = {0: rock, 1: paper, 2: scissors}
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

try:
    if user_choice not in images:
        raise ValueError
except ValueError:
    print("Invalid input. Please enter 0, 1, or 2.")
    exit()

computer_choice = random.randint(0, 2)

print("\nYour choice:")
print(images[user_choice])

print("\nComputer's choice:")
print(images[computer_choice])

if user_choice == computer_choice:
    print("It's a tie.")
elif (user_choice == 0 and computer_choice == 2) or \
        (user_choice == 1 and computer_choice == 0) or \
        (user_choice == 2 and computer_choice == 1):
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time!")
