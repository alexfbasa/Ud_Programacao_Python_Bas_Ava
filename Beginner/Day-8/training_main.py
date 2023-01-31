from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(initial_text, rotation_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        rotation_amount *= -1

    for char in initial_text:
        if char in alphabet:
            current_position = alphabet.index(char)
            new_position = current_position + rotation_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text.title()}")


should_stop = False
while not should_stop:
    get_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    get_text = input("Type your message:\n").lower()
    get_rotation_amount = int(input("Type the shift number:\n"))
    caesar(get_text, get_rotation_amount, get_direction)

    get_reset_app = input(f"Do you wan to execute the app again? type 'yes' or 'no' ").lower()
    if get_reset_app == 'yes':
        pass
    else:
        print("Goodbye")
        should_stop = True
