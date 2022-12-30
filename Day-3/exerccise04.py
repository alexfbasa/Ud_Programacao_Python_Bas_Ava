print("Welcome to the rollercoaster! ")
get_height = int(input('What is your height in cm? '))
bill = 0

if get_height > 120:
    print('You can ride the rollercoaster')
    get_age = int(input('How old are you? '))
    if get_age < 12:
        bill = 5
        print(f'You have to pay {bill}')
    elif 12 <= get_age <= 18:
        bill = 7
        print(f'You have to pay {bill}')
    else:
        bill = 12
        print(f'You have to pay {bill}')
else:
    print("Sorry, you have to grow taller before you can ride :( ")
