import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
# guess.
chosen_word = random.choice(word_list)
size_chosen_word = len(chosen_word)
print(chosen_word)
guess = input(f"It's your time, guess a letter: ").lower()

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].


panel_letter = []
for _ in range(size_chosen_word):
    panel_letter += '_'

for letter in chosen_word:
    if guess == letter:
        print('Right')
    else:
        print('Wrong')
print(panel_letter)

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace
#  with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

for position in range(size_chosen_word):
    letra = chosen_word[position]
    if letra == guess:
        panel_letter[position] = letra
print(panel_letter)

'''
palavra = alexandre
chutes = (pergunta).lower()  1 - B; 2 - c; 3 - A;
for b in range(len(palavra=9Letras)
    letra = palavra[0]
    a
    if chutes[b] == letra[a]
        panel.append(chute[posicao])
    else:
        pass
for c in range(len(palavra=9Letras, 9repeticoes)
    letra = palavra[1]
    b    
    if chutes[b] == letra[l]
        panel.append(chute[posicao])
    else:
        pass 
for A in range(len(palavra=9Letras, 9repeticoes)
    letra = palavra[1]
    b    
    if chutes[b] == letra[l]
        panel.append(chute[posicao])
    else:
        pass 
    
'''