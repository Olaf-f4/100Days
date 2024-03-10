##################### Extra Hard Starting Project ######################
import pandas as pd
import random
import datetime as dt
import smtplib

# 1. Update the birthdays.csv
birthdays = pd.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
date = dt.datetime.now()
individuals = birthdays.iloc()
day = date.day
month = date.month


def rand_letter(name):
    number = random.randint(1, 3)
    with open(f"letter_templates/letter_{number}.txt", "r") as letter:
        letter_data = letter.read()
        filedata = letter_data.replace("[NAME]", name)
        with open(f"letter_templates/letter_{name}.txt", "w") as insert:
            insert.write(filedata)

my_email = "vikingishly@gmail.com"
password = "uxpxdrmajodhfolf"

for x in individuals:
    if day == x["day"] and month == x["month"]:
        rand_letter(x["name"])
        with open(f"letter_templates/letter_{x["name"]}.txt", 'r') as message:
            message = message.read()
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email,
                                 password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs="brandonolafsen@gmail.com",
                                    msg=f"Subject: Happy birthday!\n\n{message}")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




