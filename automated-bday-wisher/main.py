import smtplib
import datetime as dt
import pandas
import random

data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
day_of_week = now.weekday()
current_month = now.month
current_day = now.day
today = (current_month, current_day)
birthdays = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
my_email = "rooteduzr@gmail.com"
email_pw = "12345"
subject = "Happy Birthday!"


if today in birthdays:
    name = birthdays[today]["name"]
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as note:
        birthday_note = note.read()
    birthday_note = birthday_note.replace('[NAME]', name)
    print(birthday_note)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=email_pw)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: {subject}\n\n{birthday_note}")
else:
    print("No Birthdays today.")
