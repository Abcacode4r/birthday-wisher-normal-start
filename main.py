##################### Normal Starting Project ######################
import random
import smtplib
import pandas

Emails = "alyseraby@gmail.com"
Passwords = "gdcikubswzdpfabi"


from datetime import datetime
today=datetime.now()
date_tuple=(today.month,today.day)
data=pandas.read_csv("birthdays.csv")
birth_days_dict={(data_row.month,data_row.day):data_row for (index,data_row) in data.iterrows()}
if date_tuple in birth_days_dict:
    birthday_person=birth_days_dict[date_tuple]
    letter=f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(letter) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])
        contents=contents.replace("Angela","Abyi")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(Emails,Passwords)
        connection.sendmail(from_addr=Emails,
                            to_addrs=birthday_person["email"],
                            msg=f"subject:Happy Birth Day\n\n{contents}")
