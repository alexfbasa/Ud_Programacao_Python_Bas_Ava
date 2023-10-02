import warnings

import requests
from tkinter import Tk, Canvas, PhotoImage, Button, Label

url = "https://api.kanye.rest/"


def get_kanye_quote():
    response = requests.get(url, verify=False)
    response.raise_for_status()
    warnings.filterwarnings("ignore", message="InsecureRequestWarning")
    kayne_quote = response.json()
    kanye_phrase = kayne_quote['quote']
    canvas.itemconfig(quote_text, text=f"{kanye_phrase}")


# GUI
window = Tk()
window.config(pady=50, padx=50)
window.title("Kanye quotes")

# Image
kanye_img = PhotoImage(file="kanye.png")
background_img = PhotoImage(file="background.png")

# Canvas
canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_img)
canvas.grid(column=0, row=0)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 30, "bold"),
                                fill="white")

# Button
kanye_button = Button(image=kanye_img, command=get_kanye_quote, highlightthickness=0)
kanye_button.grid(column=0, row=3)

get_kanye_quote()

window.mainloop()
