import smtplib

my_email = "dahun4032@gmail.com"
password = ""
# connection = smtplib.SMTP("smtp.gmail.com", port=587)
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # makes secure
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="tty4032@naver.com",

                        msg="Subject:Hello \n\n This is the body email")

