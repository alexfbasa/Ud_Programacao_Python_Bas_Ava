from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("../data/English_Words_Learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("../data/English_Portugues_Words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Portugues", fill="black")
    canvas.itemconfig(card_word, text=current_card["Portugues"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=back_card)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("../data/English_Words_Learn.csv", index=False)
    next_card()


# GUI
window = Tk()
window.title("Flasky")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Images
back_card = PhotoImage(file="../images/card_back.png")
front_card = PhotoImage(file="../images/card_front.png")
cross_image = PhotoImage(file="../images/wrong.png")
right_image = PhotoImage(file="../images/right.png")

# Canvas
canvas = Canvas(background=BACKGROUND_COLOR, width=800, height=564, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 153, text=" ", font=("ariel", 49, "italic"))
card_word = canvas.create_text(400, 263, text=" ", font=("ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)
known_button = Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
