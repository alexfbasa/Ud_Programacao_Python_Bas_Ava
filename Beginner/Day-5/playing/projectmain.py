import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
tmp_pass = []

print("Welcome to the PyPassword Generator!")
get_nr_letters = int(input("How many letters would you like in your password?\n"))
get_nr_numbers = int(input("How many numbers would you like?\n"))
get_nr_symbols = int(input("How many symbols would you like?\n"))

for char in range(0, get_nr_numbers):
    character = random.choice(letters)
    tmp_pass.append(character)

for num in range(0, get_nr_numbers):
    number = random.choice(numbers)
    tmp_pass.append(number)

for sym in range(0, get_nr_symbols):
    symbol = random.choice(symbols)
    tmp_pass.append(symbol)


final_pass = ''.join(str(i) for i in tmp_pass)
print(f"Your password has {len(final_pass)} characters and it's: {final_pass}")
