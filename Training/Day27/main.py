from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text='My label', font=("Arial", 22, 'bold'))
my_label.pack(side='top')


def print_message_button():
    my_label['text'] = "I got clicked"
    my_label.pack()


my_label['text'] = 'New text'

button = Button(text='Click ME', command=print_message_button)
button.pack()

window.mainloop()
