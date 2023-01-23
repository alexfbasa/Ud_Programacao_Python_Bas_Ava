def add(*args):
    number = 0
    for n in args:
        number += n
    return number


# eight_numbers = add(1, 2, 3, 4, 5, 5, 7, 34)
# four_numbers = add(4, 5, 5, 7)
# three_numbers = add(1, 2, 3)
# print(eight_numbers)
# print(four_numbers)
# print(three_numbers)

def calculate(n, **kwargs):
    print(kwargs)
    # for k, v in kwargs.items():
    #     print(k)
    #     print(v)
    print(kwargs['add'], kwargs['multiply'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


print(calculate(5, add=3, multiply=5))
