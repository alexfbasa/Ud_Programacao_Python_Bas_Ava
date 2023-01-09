from replit import clear

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(initial_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    else:
        pass
    for char in initial_text:
        if char in alphabet:
            position_in_alphabet = alphabet.index(char)
            new_alphabet_position = shift_amount + position_in_alphabet
            end_text += alphabet[new_alphabet_position]
    print(f"Here's the {cipher_direction}d result: {end_text}")


end_app = False


while not end_app:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    check_run_again = input(f"Do you wan to run the Caesar cipher again? 'yes', 'no' ")
    if check_run_again == 'no':
        end_app = True
    else:

        clear()
