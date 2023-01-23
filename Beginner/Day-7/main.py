import random

from hangman_art import logo, stages
from hangman_words import word_list

compliment_words = ['Good job.', 'Nice shoot.', 'Keep doing.', 'Almost done.']
print(logo)

choose_word = random.choice(word_list)
print(choose_word)

word_board = []
for x in choose_word:
    word_board.append('_')

print(f'The secret word has {len(choose_word)} characters:')
print(word_board)
game_is_on = True
lives = 6

while game_is_on:
    get_guess = input('Guess a letter: ').lower()
    if get_guess in word_board:
        print('You have already guesses that letter. ')

    tem_compliment = random.choice(compliment_words)

    for position in range(len(choose_word)):
        temp_letter = choose_word[position]
        if temp_letter == get_guess:
            word_board[position] = temp_letter

    if get_guess not in choose_word:
        lives -= 1
        print(f"That letter is not contained in the secret word, you lose a life. You have {lives}/6")
        if lives == 0:
            print('You lose. ')
            game_is_on = False
    print(f"{' '.join(word_board)}")

    if '_' not in word_board:
        print(f'You got it. Congratulation!! ')
        game_is_on = False

    print(stages[lives])

print(f"The secret word was {choose_word}.")
