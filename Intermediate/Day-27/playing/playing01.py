from tkinter import *

screen = Tk()
screen.minsize(width=500, height=300)
screen.title("My screen")

my_label = Label(text=f"I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def clicked():
    new_text = user_input.get()
    my_label["text"] = f"{new_text}"


button = Button(text="Click ME", command=clicked)
button.pack()

user_input = Entry()
user_input.pack()


screen.mainloop()
