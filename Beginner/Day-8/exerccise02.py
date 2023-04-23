alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

length_alphabet_list = len(alphabet)


# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        posicao = alphabet.index(letter)
        nova_posicao = posicao + shift_amount
        nova_letra = alphabet[nova_posicao]
        cipher_text += nova_letra
    print(cipher_text)


def decrypt(crypt_text, shift_amount):
    decrypted_text = ""
    for letter in crypt_text:
        posicao = alphabet.index(letter)
        antiga_posicao = posicao - shift_amount
        antiga_letra = alphabet[antiga_posicao]
        decrypted_text += antiga_letra
    print(decrypted_text)


# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the
#  alphabet by the shift amount and print the encrypted text.
# e.g.
# plain_text = "hello"
# shift = 5
# cipher_text = "mjqqt"
# print output: "The encoded text is mjqqt"

# HINT: How do you get the index of an item in a list:
# https://www.w3schools.com/python/ref_list_index.asp
# https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛



# encrypt(plain_text=text, shift_amount=shift)
#
# decrypt(crypt_text=input('Text'), shift_amount=shift)
