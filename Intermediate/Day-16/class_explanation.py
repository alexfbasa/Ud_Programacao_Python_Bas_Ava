# from turtle import Turtle, Screen
# import prettytable
#
# crush = Turtle()
# print(crush)
# my_screen = Screen()
# crush.shape("turtle")
# crush.shapesize(5)
# crush.forward(150)
#
# # Objects and Attributes
# print(my_screen.canvheight)
#
# # Methods
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Raichu', 'Sandshrew'])
table.add_column("Type", ['Electric', 'Electric', 'Ground'])
table.align = 'l'
print(table)
