from art import logo

print(logo)


def soma(num01, num02):
    return num01 + num02


def subtrair(num01, num02):
    return num01 - num02


def multi(num01, num02):
    return num01 * num02


def dividir(num01, num02):
    return num01 / num02


get_number01 = int(input("What's the first number?: "))
get_operacao = input("What is the operation to perform?:")
get_number02 = int(input("What's the second number?: "))

operacoes = {
    "+": soma,
    "-": subtrair,
    "*": multi,
    "/": dividir,
}


def calculando(num01, operacao, num02):
    if operacao in operacoes:
        resultado = operacoes[operacao](num01, num02)
        return resultado
    else:
        return "Invalid operation"


result = calculando(get_number01, get_operacao, get_number02)
print(f"The operation's result is: {result}")
