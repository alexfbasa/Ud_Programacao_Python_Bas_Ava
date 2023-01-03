programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}
print(programming_dictionary['Bug'])
print('Bug"', programming_dictionary['Bug'])

print(programming_dictionary['Function'])
programming_dictionary['Loop'] = 'The action of doing something over and over again.'

print(programming_dictionary['Loop'])

'''
Para adicionar novos itens 
programming_dictionary['novo_item' = 'Item"
Para iterar no dicionario ele trara  key ao inves do valor
'''
for key in programming_dictionary:
    print(key)
'''
Bug
Function
Loop
Ou pode pegar o item atraver da key 
'''
for key in programming_dictionary:
    # A key sera as chaves = Bug, Loop e Function, entao ele imprimar o valor :)
    print(programming_dictionary[key])
    print(key, programming_dictionary[key])

# Nesting
capitals = {
    'France': 'Paris',
    'Brazil': 'Brasilia'
}

tavel_log = {
    'France': ["Paris", 'Lille', 'Dijon'],
    'Germany': ["Berlim", "Hamburg", "Stuttgart"],
    'Brazil': ['Campo Grande', 'Bonito', 'Salvador']
}
# Nesting Dictionary in a Dictionary
tavel_log_2 = {
    'France': {'cities_visited': ["Paris", 'Lille', 'Dijon'], 'total_visits': 23},
    'Germany': ["Berlim", "Hamburg", "Stuttgart"],
    'Brazil': ['Campo Grande', 'Bonito', 'Salvador']
}

tavel_log_3 = {
    "Brasil": {'Cidades famosas': ['Rio de Janeior', 'Florianopolis', 'Salvador', 'Gramado'],
               'Comidas famosas': ['Frango com quiboa', 'Leitao a pururuca', 'Galinha com pequi'],
               'total_visits': 0},
    "Mexico": {'Cidades famosas': ['Cidade do Mexico', 'Cancun', 'Puerto Vallarta', 'Tulum'],
               'Comidas famosas': ['Guacamole', 'Tacos', 'Tortilhas', 'Chilli com carne', 'Burrito'],
               'total_visits': 0}
}
# Multiples dictionaries inside a list
test = [{
    "Key01": ["List", ],
    "Key02": {"Dict": 0},
},
    {
        "Key03": ["List", ],
        "Key04": {"Dict": 0},
    }]
# List two items each item is a dictionary
tavel_log_4 = [
    {"country": "Brasil",
     "Cidades famosas": ['Rio de Janeior', 'Florianopolis', 'Salvador', 'Gramado'],
     'total_visits': 0},
    {"country": "Mexico",
     "Cidades famosas": ['Cidade do Mexico', 'Cancun', 'Puerto Vallarta', 'Tulum'],
     'total_visits': 0},
]
