from tkinter import *


def clicked():
    new_text = user_input.get()
    my_label["text"] = f"{new_text}"


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text=f"I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click ME", command=clicked)
button.grid(column=1, row=1)
# Entry
user_input = Entry()
print(user_input.get())
user_input.grid(column=1, row=2)

window.mainloop()
