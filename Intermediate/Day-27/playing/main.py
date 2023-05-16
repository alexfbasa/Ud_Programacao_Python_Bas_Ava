from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def convert_mile_km():
    miles = float(miles_input.get())
    km = round(miles * 1.606, 2)
    kilometer_result_label.config(text=f"{km}")


miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="Km")
kilometer_result_label.grid(column=1, row=1)

button = Button(text="Calculate", command=convert_mile_km)
button.grid(column=2, row=1)


window.mainloop()
