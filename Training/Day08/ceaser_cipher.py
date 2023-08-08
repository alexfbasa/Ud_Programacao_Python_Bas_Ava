# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']


def caesar_cipher(direction, text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def get_shifted_position(initial_position, shift_amount):
        if direction == 'encode':
            return (initial_position + shift_amount) % 26
        elif direction == 'decode':
            return (initial_position - shift_amount) % 26

    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            initial_letter_position = alphabet.index(letter)
            new_letter_position = get_shifted_position(initial_letter_position, shift)
            shift_letter_position = alphabet[new_letter_position]
            cipher_text += shift_letter_position
        else:
            cipher_text += letter

    return cipher_text


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

result = caesar_cipher(direction, text, shift)
print(result)
