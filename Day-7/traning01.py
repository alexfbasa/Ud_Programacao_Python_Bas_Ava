# Step 1
import random
from hangman_art import stages, logo
print(logo)
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
images = stages
display = []
end_of_game = False
lives = 6

for item in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    print(lives)
    if guess in display:
        print(f"You've already guessed {guess} letter.")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guesses {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            end_of_game = True
    print(lives)
    if '_' not in display:
        print('Congratulations! You win.')
        end_of_game = True
    else:
        pass
    print(images[lives])
print(display)
