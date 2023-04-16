from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# DEBUG
# Give me the position number
print(alphabet.index('a'))
# Give me the letter in the position number
print(alphabet[0])

print(logo)

is_cipher_app_on = True


def encrypt(operator, text, shift):
    encrypt_text = ""
    if operator == 'decode':
        shift *= -1
    for l in text:
        if l in alphabet:
            l_position = alphabet.index(l)
            new_char_position = l_position + shift
            encrypt_text += alphabet[new_char_position]
    return encrypt_text


def show_final_message(initial_text, text_cipher):
    return f"Here's the {text_cipher} result: {initial_text}"


while is_cipher_app_on:
    get_user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    get_user_message = input("Type your message: \n").lower()
    get_shit_number = int(input("Type the shift number:"))
    text_cipher = encrypt(get_user_choice, get_user_message, get_shit_number)
    result = show_final_message(get_user_message, text_cipher)
    print(result)
    should_continue = input("Do you want to run it again? (Yes) (No) ").lower()
    if should_continue == 'yes':
        pass
    else:
        print("GoodBye :) ")
        is_cipher_app_on = False
