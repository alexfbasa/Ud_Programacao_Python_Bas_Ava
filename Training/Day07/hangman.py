import random

EASY_MODE = 10
HARD_MODE = 5

word_list = [
    "apple", "banana", "computer", "elephant", "fantastic",
    "gravity", "holiday", "igloo", "jigsaw", "kangaroo",
    "lemon", "mountain", "necklace", "octopus", "pineapple",
    "question", "rainbow", "strawberry", "tiger", "umbrella",
    "vacation", "watermelon", "xylophone", "yak", "zebra"
]

get_word = random.choice(word_list)
secret_word = ['_'] * len(get_word)

print(" ".join(secret_word))
print(get_word)

get_user_level = input('Choose your mode level: H - Hard, E - Easy.').lower()

if get_user_level == 'e':
    game_level = EASY_MODE
else:
    game_level = HARD_MODE

while '-' in secret_word and game_level > 0:
    get_user_letter = input('Guess a letter: ').lower()

    if get_user_letter in secret_word:
        print("You've already guessed this letter.")
        continue

    found = False
    for i, l in enumerate(get_word):
        if l == get_user_letter:
            secret_word[i] = get_user_letter
            found = True

    if not found:
        game_level -= 1
        print(f"Wrong guess! You have {game_level} {'guesses' if game_level > 1 else 'guess'} left.")

    print(" ".join(secret_word))

if '-' not in secret_word:
    print("Congratulations! You've guessed the word!")
else:
    print(f"Sorry, you're out of guesses. The word was '{get_word}'.")
