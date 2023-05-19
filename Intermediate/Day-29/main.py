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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    if website == "" or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")

    else:
        get_user_choice = messagebox.askokcancel(title=website,
                                                 message=f"These are the details entered: \nEmail: {email}"
                                                         f"Password: {password} \nIs it okay to save? ")
        if get_user_choice:
            with open('data.txt', mode='a') as file_data:
                file_data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
app_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=app_logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

# Entries
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, string="alexsimple@gmail.com")
password_entry = Entry(width=21)

password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
