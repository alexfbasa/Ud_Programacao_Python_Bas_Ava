with open("file01.txt") as file01:
    number01 = file01.readlines()

with open("file02.txt") as file02:
    number02 = file02.readlines()


numbers = [int(n) for n in number01 if n in number02]

print(numbers)

number_plus = [n * 2 for n in numbers]

print(number_plus)
