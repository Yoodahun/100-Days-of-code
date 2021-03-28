import smtplib
import datetime as dt
import random

my_email = ""
password = ""
# connection = smtplib.SMTP("smtp.gmail.com", port=587)

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

# quoetes_list = []

# with open("quotes.txt") as quoetes_list_text:
    # quoetes_list = [quoetes_list_text.readline() for _ in len(quoetes_list_text)]

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # makes secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg=f"Subject:Todays quotes \n\n {quote}")

