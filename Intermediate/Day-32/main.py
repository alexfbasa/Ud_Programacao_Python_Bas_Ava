import datetime as dt
import random
import smtplib

gmail_address = "email@gmail.com"
gmail_pass = "password"

current_date = dt.datetime.now()
weekday = current_date.weekday()
day_name = current_date.strftime("%A")

if weekday == 2:
    with open("quotes.txt", "r") as file_msg:
        msg = random.choice(file_msg.readlines())
        # Send email
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=gmail_address, password=gmail_pass)
        connection.sendmail(from_addr=gmail_address, to_addrs="test@proton.me",
                            msg=f"Subject: Friendly {day_name} reminder. \n\n{msg}.")
