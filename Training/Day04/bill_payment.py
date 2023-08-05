import random

get_names = input('Type the names separated by comma:')
names = get_names.split(',')

choice_person = random.choice(names)
print(f" Who is going to pay the bill tonight is {choice_person}")

