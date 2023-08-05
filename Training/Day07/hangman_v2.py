import random

EASY_MODE = 10
HARD_MODE = 5


def initialize_game():
    word_list = [
        "apple", "banana", "computer", "elephant", "fantastic",
        "gravity", "holiday", "igloo", "jigsaw", "kangaroo",
        "lemon", "mountain", "necklace", "octopus", "pineapple",
        "question", "rainbow", "strawberry", "tiger", "umbrella",
        "vacation", "watermelon", "xylophone", "yak", "zebra"
    ]

    get_game_level = input("Choose your game level: E - Easy, H - Hard: ").lower()
    if get_game_level == 'e':
        game_lives = EASY_MODE
    elif get_game_level == 'h':
        game_lives = HARD_MODE
    else:
        print('Option invalid: Type E or H.')
        exit()

    secret_word = random.choice(word_list)
    display = ['_'] * len(secret_word)

    return secret_word, display, game_lives


def main():
    secret_word, display, game_lives = initialize_game()

    print(" ".join(display))

    while '_' in display and game_lives > 0:
        user_guess = input('Guess a letter:').lower()
        if user_guess in display:
            print("You've already guessed this letter.")
            continue

        found = False
        for i, l in enumerate(secret_word):
            if l == user_guess:
                display[i] = user_guess
                found = True

        if not found:
            game_lives -= 1
            print(f"Wrong guess! You have {game_lives} {'guesses' if game_lives > 1 else 'guess'} left.")

        print(" ".join(display))

    if '_' not in display:
        print("Congratulations! You've guessed the word!")
    else:
        print(f"Sorry, you're out of guesses. The word was '{secret_word}'.")


if __name__ == "__main__":
    main()
