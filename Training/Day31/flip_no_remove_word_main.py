import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/English_Portugues_Words.csv")
to_learn = data.to_dict(orient="records")
current_card = {

}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    portugues_word = current_card['Portugues']
    canvas.itemconfig(card_title, text="Portugues", fill='black')
    canvas.itemconfig(card_word, text=portugues_word)
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


# GUI
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Images
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text=" ", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, command=next_card, highlightthickness=0)
unknown_button.grid(column=0, row=3)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, command=next_card, highlightthickness=0)
known_button.grid(column=1, row=3)

next_card()
window.mainloop()
