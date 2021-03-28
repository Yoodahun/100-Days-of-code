##################### Normal Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

# 2. Check if today matches a birthday in the birthdays.csv

today = (dt.datetime.now().month, dt.datetime.now().day)
data = pandas.read_csv("birthdays.csv")
my_email = ""
password = ""

birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict[today])

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in birthdays_dict:
    picked_template = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(picked_template) as letter_template:
        letter = letter_template.read().replace("[NAME]", birthdays_dict[today]["name"])
        # letter.replace("[NAME]", birthdays_dict[today]["name"])
    to_email_address = birthdays_dict[today]["email"]


# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # makes secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email_address,
                            msg=f"Subject:Happy birthday \n\n {letter}")




