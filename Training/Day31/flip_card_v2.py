import tkinter as tk
from tkinter import PhotoImage
from gtts import gTTS
import random
import pandas as pd
import os

BACKGROUND_COLOR = "#B1DDC6"
CSV_FILE = "data/English_Portugues_Words.csv"


class FlashcardApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Flashy")
        self.window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

        self.load_data()
        self.current_card = None
        self.flip_timer = None

        self.create_widgets()
        self.show_next_card()

    def load_data(self):
        if os.path.exists(CSV_FILE):
            self.data = pd.read_csv(CSV_FILE)
        else:
            self.data = pd.read_csv("data/English_Portugues_Words_default.csv")

        self.to_learn = self.data.to_dict(orient="records")

    def create_widgets(self):
        # Canvas for flashcard
        self.canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.card_front_img = PhotoImage(file="images/card_front.png")
        self.card_back_img = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.card_title = self.canvas.create_text(400, 90, text=" ", font=("Arial", 40, "italic"))
        self.card_word = self.canvas.create_text(400, 175, text=" ", font=("Arial", 60, "bold"))

        # Buttons
        self.cross_img = PhotoImage(file="images/wrong.png")
        self.unknown_button = tk.Button(image=self.cross_img, command=self.show_next_card, highlightthickness=0)
        self.unknown_button.grid(column=0, row=1)

        self.check_img = PhotoImage(file="images/right.png")
        self.known_button = tk.Button(image=self.check_img, command=self.known_card, highlightthickness=0)
        self.known_button.grid(column=1, row=1)

        self.pronounce_img = PhotoImage(file="images/pronounce_img.png", width=60, height=60)
        self.pronounce_button = tk.Button(image=self.pronounce_img, command=self.play_pronunciation)
        self.pronounce_button.grid(column=1, row=3)

        self.arrow_back_img = PhotoImage(file="images/arrow-back-3783.png")
        self.back_button = tk.Button(image=self.arrow_back_img, command=self.show_last_card, text="Get last word")
        self.back_button.grid(column=1, row=0)

        # Pronunciation entry and label
        self.entry_label = tk.Label(text="Pronunciation:", font=("Arial", 20, "bold"))
        self.entry_label.grid(column=0, row=2, padx=(10, 0), pady=(10, 0))
        self.entry_pronunciation = tk.Entry(width=60)
        self.entry_pronunciation.grid(column=1, row=2, columnspan=2, padx=(0, 10), pady=(10, 0))

    def show_next_card(self):
        if self.flip_timer is not None:
            self.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.to_learn)
        self.update_card(self.current_card)

    def show_last_card(self):
        self.window.after_cancel(self.flip_timer)
        if self.current_card:
            self.update_card(self.current_card)

    def known_card(self):
        if self.current_card:
            self.to_learn.remove(self.current_card)
            self.save_progress()
            self.show_next_card()

    def update_card(self, card):
        self.canvas.itemconfig(self.card_title, text="Portugues", fill='black')
        self.canvas.itemconfig(self.card_word, text=card['Portugues'], fill="black")
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English", fill='white')
        self.canvas.itemconfig(self.card_word, text=self.current_card['English'], fill='white')
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)

    def play_pronunciation(self):
        if self.current_card:
            pronunciation = self.current_card.get('Pronunciation', '')
            if pronunciation:
                # Play the stored pronunciation
                tts = gTTS(text=pronunciation, lang='en')
                tts.save("pronunciation.mp3")
                os.system("mpg123 pronunciation.mp3")
            else:
                # If no stored pronunciation, play a default message
                tts = gTTS(text="Pronunciation not available.", lang='en')
                tts.save("pronunciation.mp3")
                os.system("mpg123 pronunciation.mp3")

    def save_progress(self):
        updated_data = pd.DataFrame(self.to_learn)
        updated_data.to_csv(CSV_FILE, index=False)


if __name__ == "__main__":
    window = tk.Tk()
    app = FlashcardApp(window)
    window.mainloop()
