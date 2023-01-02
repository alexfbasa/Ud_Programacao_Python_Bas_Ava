def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def get_flag():
    for step in range(0, 6):
        jump()

# Ou
while not at_goal():
    jump()
get_flag()
