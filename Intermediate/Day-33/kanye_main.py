from tkinter import *
import warnings
import requests


def get_quote():
    api = requests.get(url="https://api.kanye.rest/", verify=False)
    api.raise_for_status()
    warnings.filterwarnings("ignore", message="Unverified HTTPS request")
    api_json = api.json()
    kanye_quote = api_json['quote']
    canvas.itemconfig(quote_text, text=f"{kanye_quote}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 25, "bold"),
                                fill="white")

canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
get_quote()





window.mainloop()
