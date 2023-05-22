fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("IndexError")
    else:
        print(fruit + " pie")


make_pie(4)
