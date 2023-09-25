from tkinter import *


def mile_to_km():
    value = float(miles_entry.get())
    calc = value * 1.609
    km_result_label['text'] = calc


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_entry = Entry()
miles_entry.grid(column=1, row=0)
miles_entry.config(width=10)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text='0')
km_result_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
