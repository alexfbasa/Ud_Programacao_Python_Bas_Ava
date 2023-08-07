import random
from hangman_words import word_list
from hangman_art import logo, stages

LIVES = 6

secret_word = random.choice(word_list)
display = ['_'] * len(secret_word)
print(logo)
print(" ".join(display))

while LIVES > 0 and '_' in display:
    user_guess = input('Guess a letter:').lower()
    if user_guess in display:
        print("You've already guessed this letter!")
    else:
        found = False
        for i, l in enumerate(secret_word):
            if l == user_guess:
                display[i] = user_guess
                found = True
        if not found:
            LIVES -= 1
            print(stages[LIVES])
            print(f"There is no {user_guess} in this word.")
        else:
            print(" ".join(display))

if '_' not in display:
    print("Congratulations! You've guessed the word!")
else:
    print("Sorry, you're out of lives. The word was:", secret_word)
