# import smtplib
#
# my_email = "vikingishly@gmail.com"
# password = "uxpxdrmajodhfolf"
#
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="Brandonolafsen@gmail.com",
#                         msg="Subject: Hello\n\nThis is the body of my email.",
#                         )
#
#
# import datetime as dt
# import smtplib

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year= 2025, month=12, day=15)
# print(date_of_birth)


import datetime as dt
import smtplib
import random

date = dt.datetime.now()
my_email = "vikingishly@gmail.com"
password = "uxpxdrmajodhfolf"

with open("quotes.txt", 'r') as messages:
    message_list = messages.readlines()
    if date.day == 10:
        rm = random.choice(message_list)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="brandonolafsen@gmail.com",
                                msg=f"Subject: Day of the Week\n\n{rm}")