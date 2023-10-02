from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    load_original_data = pandas.read_csv("data/English_Portugues_Words.csv")
    to_learn = load_original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Portugues", fill='black')
    canvas.itemconfig(card_word, text=current_card['Portugues'], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)


def last_word():
    global flip_timer
    current_word = current_card['Portugues']
    print(current_word)
    canvas.itemconfig(card_title, text="Portugues", fill='white')
    canvas.itemconfig(card_word, text=f"{current_word}", fill='white')
    canvas.itemconfig(card_background, image=card_back_img)
    flip_timer = window.after(3000, func=flip_card)


def add_pronunciation():
    global current_card
    pronunciation = entry_pronunciation.get()

    # Update the current_card with the pronunciation
    current_card['Pronunciation'] = pronunciation

    # Append the word and its pronunciation to the CSV file
    with open("data/English_Portugues_Words.csv", "a") as file:
        file.write(f"\n{current_card['Portugues']},{current_card['English']},{pronunciation}")

    # Clear the entry field
    entry_pronunciation.delete(0, END)


def last_word_with_pronunciation():
    global flip_timer, current_card

    current_word = current_card['Portugues']
    pronunciation = current_card.get('Pronunciation', '')  # Get the pronunciation if it exists

    canvas.itemconfig(card_title, text="Portugues", fill='white')
    canvas.itemconfig(card_word, text=f"{current_word}", fill='white')
    canvas.itemconfig(card_pronunciation, text=f"Pronunciation: {pronunciation}", fill='white')  # Display pronunciation
    canvas.itemconfig(card_background, image=card_back_img)

    flip_timer = window.after(3000, func=flip_card)

window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 90, text=" ", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 175, text=" ", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=1, columnspan=2)
card_pronunciation = canvas.create_text(400, 350, text="", font=("Ariel", 20, "italic"))

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_img, command=next_card, highlightthickness=0)
unknown_button.grid(column=0, row=3)

check_img = PhotoImage(file="images/right.png")
known_button = Button(image=check_img, command=next_card, highlightthickness=0)
known_button.grid(column=1, row=3)

pronounce_img = PhotoImage(file="images/pronounce_img.png", width=60, height=60)
pronounce_button = Button(image=pronounce_img)
pronounce_button.grid(column=0, row=4, columnspan=2, pady=(0, 10))

arrow_back_img = PhotoImage(file="images/arrow-back-3783.png")
back_button = Button(image=arrow_back_img, command=last_word_with_pronunciation, text="Get last word")
back_button.grid(column=1, row=0)

pronunciation_label = Label(text="Pronunciation:", font=("Arial", 20, "bold"))
pronunciation_label.grid(column=0, row=2, padx=(10, 0), pady=(10, 0))

entry_pronunciation = Entry(width=60)
entry_pronunciation.grid(column=1, row=2, columnspan=2, padx=(0, 10), pady=(10, 0))

next_card()
last_word()
window.mainloop()
