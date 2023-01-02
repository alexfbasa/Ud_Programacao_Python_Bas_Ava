alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

length_alphabet_list = len(alphabet)


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


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(crypt_text=text, shift_amount=shift)
