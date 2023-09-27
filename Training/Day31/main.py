import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/English_Portugues_Words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


# GUI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas()
canvas.config(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0)

# Images
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")



window.mainloop()