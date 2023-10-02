from tkinter import *


def print_label():
    user_input = input.get()
    label['text'] = user_input


window = Tk()
window.minsize(width=500, height=300)

window.title("My first GUY program.")
label = Label(text="My Label")
label.grid(column=0, row=0)

button = Button(text="Click me", command=print_label)
button.grid(column=1, row=1)

new_button = Button(text='Button 02', command=print_label)
new_button.grid(column=2, row=0)


input = Entry(width=20)
input.grid(column=3, row=2)
window.mainloop()
