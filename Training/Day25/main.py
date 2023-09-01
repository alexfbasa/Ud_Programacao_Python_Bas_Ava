from turtle import Screen

screen = Screen()
screen.setup(800, 600)


def show_x_y(x, y):
    print(x, y)


screen.onclick(show_x_y)

screen.mainloop()
