# Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
length_chosen_word = len(chosen_word)
print(chosen_word)
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        print('Right')
    else:
        print('Wrong ')
