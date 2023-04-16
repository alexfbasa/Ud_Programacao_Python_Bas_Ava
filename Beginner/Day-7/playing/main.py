import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)
get_images_list = stages
get_words = word_list
get_random_word = random.choice(get_words)
print(f"The secret word is {get_random_word}")
display_secret_chars = []
is_game_on = True
LIVES = 6

for l in get_random_word:
    display_secret_chars.append("_")

print(display_secret_chars)

while is_game_on:
    print(get_images_list[LIVES])
    get_user_letter = input('Choice a letter: ').lower()
    if get_user_letter in display_secret_chars:
        print("You've already guessed this letter.")
        LIVES -= 1
    for position in range(len(get_random_word)):
        letter = get_random_word[position]
        if letter in get_user_letter:
            display_secret_chars[position] = letter
    print("You've got a right shoot!!")
    print(display_secret_chars)
    if get_user_letter not in get_random_word:
        LIVES -= 1
        print(f"There is no letter {get_user_letter} in the secret word.")
        print(f"You lost a live. You have {LIVES} lives.")
        if LIVES == 0:
            print("Your lives are over.")
            print("Game over.")
            is_game_on = False
    if '_' not in display_secret_chars:
        is_game_on = False
        print("Congratulations you win.")
    # print(get_random_word[LIVES])
