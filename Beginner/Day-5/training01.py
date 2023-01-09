'''
Instructions
You are going to write a program that calculates the average student height from a List of heights.
The average height can be calculated by adding all the heights together and dividing by the total number of heights.
'''
# Recebe a altura dos estudantes como um strig o split ira dividir cada altura pela virgula
# estudantes_altura virara uma lista de string
estudantes_altura = input('Digite a altura dos estudantes: ').split(',')

# converte a lista estudante altura de String para inteiro. Pega cada valor e cria um indice
# para poder converter
for altura in range(0, len(estudantes_altura)):
    estudantes_altura[altura] = int(estudantes_altura[altura])

soma_altura = 0

for valor in estudantes_altura:
    soma_altura += valor

print(soma_altura)
