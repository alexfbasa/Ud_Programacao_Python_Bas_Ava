import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
lista_senha = []
for letra in range(0, nr_letters):
    lista_senha.append(random.choice(letters))

for letra in range(0, nr_numbers):
    numero_randomico = random.choice(numbers)
    lista_senha.append(numero_randomico)
    if numero_randomico in lista_senha:
        pass
    else:
        lista_senha += numero_randomico

for letra in range(0, nr_symbols):
    simbolo_randomico = random.choice(symbols)
    lista_senha.append(simbolo_randomico)
    if simbolo_randomico in lista_senha:
        pass
    else:
        lista_senha += simbolo_randomico

password = ""
random.shuffle(lista_senha)
print(lista_senha)


for char in lista_senha:
    password += char

print(f"Your password is: {password}")
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
