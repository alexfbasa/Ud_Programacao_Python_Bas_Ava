alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cipher(plan_text, shift_amount, cipher_direction):
    secret_text = ""
    for letter in plan_text:
        if letter in alphabet:
            current_letter_position = alphabet.index(letter)
            if cipher_direction.lower() == 'encode':
                new_position = (current_letter_position + shift_amount) % 26
            elif cipher_direction.lower() == "decode":
                new_position = (current_letter_position - shift_amount) % 26
            new_letter = alphabet[new_position]
            secret_text += new_letter
        else:
            secret_text += letter
    print(f"The {cipher_direction}d text is: {secret_text}")


cipher(text, shift, direction)
