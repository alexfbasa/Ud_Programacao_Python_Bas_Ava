import string
from tkinter import *
import random
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------------ #

def save_password():
    website_typed = website_entry.get().title()
    password_typed = password_entry.get()
    email_typed = email_username_entry.get()

    if website_typed and password_typed and email_typed:
        is_it_ok = messagebox.askokcancel(title=email_typed,
                                          message=f"These are the details entered: \nEmail: {email_typed}"
                                                  f"\nPassword: {password_typed}\nIs it ok to save.")
        if is_it_ok:
            with open('passbolt.txt', 'a') as file_output:
                file_output.write(f"{website_typed} | {password_typed} | {email_typed}\n")

                website_entry.delete(0, END)
                password_entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Please fill in all fields.")


# ---------------------------- UI SETUP ----------------------------------------- #

# Window
window = Tk()
window.title("My password manager:")
window.config(padx=50, pady=50)

logo_image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username: ")
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_username_entry = Entry(width=35)
email_username_entry.insert(END, string="alexsimple@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=24)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3, columnspan=1)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
