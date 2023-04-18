from art import logo

print(logo)
is_calc_on = True


def add(n01, n02):
    return n01 + n02


def minus(n01, n02):
    return n01 - n02


def multi(n01, n02):
    return n01 * n02


def div(n01, n02):
    return n01 / n02


operations_signals = {
    "+": add,
    "-": minus,
    "*": multi,
    "/": div,
}
get_first_number = float(input("What's the first number?: "))
while is_calc_on:
    for k in operations_signals:
        print(k)
    get_operation = input("Choice an operation:")
    get_second_number = float(input("What's the second number?: \n"))
    calculation_function = operations_signals[get_operation]
    answer = calculation_function(get_first_number, get_second_number)
    print(f"{get_first_number} {get_operation} {get_second_number} = {answer}")
    get_user_continue = input("Do you want to calculate some other number? Type (Yes) (No)").lower()
    if get_user_continue == "yes":
        get_first_number = answer
        pass
    else:
        is_calc_on = False
