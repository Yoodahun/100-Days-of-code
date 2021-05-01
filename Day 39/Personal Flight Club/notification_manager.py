import smtplib
from data_manager import DataManager


class NotificationManager:

    def __init__(self):
        self.data_mg = DataManager()
        pass

    def notification(self, message):
        print(message)

    def send_email(self, message, departure_airport, arrive_airport, out_date, return_date):
        my_email = "tty4032@likelion.org"
        password = "ekgns123!"
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()  # makes secure
        connection.login(user=my_email, password=password)

        search_url = f"https://www.google.com/flight?hl=en#flt={departure_airport}.{arrive_airport}.{out_date}" \
                     f"*{departure_airport}.{arrive_airport}.{return_date}"

        for user in self.data_mg.get_excel_user_data():
            connection.sendmail(from_addr=my_email,
                                to_addrs=user["email"],
                                msg=f"Subject:New Low Price Flight \n\n "
                                    f"Dear {user['firstName']} \n {message} \n {search_url}".encode('utf-8')
                                )
        connection.close()
