import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    """Get a mouse click and print out the X and Y location on the screen."""
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()

# screen.exitonclick()
