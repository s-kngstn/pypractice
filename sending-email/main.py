# ------------ Sending Email ------------------------------------#
# import smtplib

# my_email = "rootaccesss@yahoo.com"
# yahoopw = "xkhcbijarfdbnqlh"
# gmailpw = "@s12345k!"
# message = "Subject: Hello!!!\n\nHello this is the body of my email"
# 
# gmail_smtp = "smtp.gmail.com"
# yahoo_smtp = "smtp.mail.yahoo.com"
# 
# with smtplib.SMTP(yahoo_smtp) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=yahoopw)
#     connection.sendmail(from_addr=my_email, to_addrs="rooteduzr@gmail.com", msg=message)
# 
# --------------- Date & Time ------------------------ #
# import datetime as dt
# 
# now = dt.datetime.now()
# year = now.year
# if year == 2021:
#     print("Happy new year!")
# month = now.month
# day = now.day
# hour = now.hour
# minute = now.minute
# sec = now.second
# day_of_week = now.weekday()
# date_of_birth = dt.datetime(year=1985, month=4, day=23)
# print(date_of_birth)

import datetime as dt
import smtplib
import random
import codecs

now = dt.datetime.now()
day_of_week = now.weekday()
sunday = 0

my_email = "rooteduzr@gmail.com"
pw = "@s12345k!"

if day_of_week == sunday:
    with open("quotes.txt") as file:
        quote_list = file.readlines()
        quote = random.choice(quote_list)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=pw)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Motivation\n\n{quote}")