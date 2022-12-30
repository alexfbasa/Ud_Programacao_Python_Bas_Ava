from art import LOGO

print(f'Welcome to the {LOGO}')
print("Welcome to Treasure Island.")

is_game_on = True
while is_game_on:
    print("Your mission is to find the treasure.")
    get_first_way = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'. ").lower()
    if get_first_way == 'left':
        get_second_way = input(
            f"You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat."
            f" Type 'swim' to swim across ").lower()
        if get_second_way == 'wait':
            get_third_way = input(f"You arrive at the island unharmed. There is a house with 3 doors."
                                  f"One red, one yellow and one blue. Which colour do you choose?").lower()
            if get_third_way == 'yellow':
                print('You found the treasure! You Win!')
                is_game_on = False
            elif get_third_way == 'blue':
                print('You enter a room of beasts. Game Over.')
                is_game_on = False
            elif get_third_way == 'red':
                print("It's a room full of fire. Game Over.")
                is_game_on = False
        elif get_second_way == 'swim':
            print('You get attacked by an angry trout. Game Over.')
            is_game_on = False
        else:
            print('Parameter invalid ')
    elif get_first_way == 'right':
        print('You fell into a hole. Game Over.')
        is_game_on = False
    else:
        print('Parameter invalid ')
