from twilio.rest import Client
from data_manager import DataManager
import smtplib
import os

TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = os.environ["TWILIO_VIRTUAL_NUMBER"]
TWILIO_VERIFIED_NUMBER = os.environ["TWILIO_VERIFIED_NUMBER"]

MY_MAIL = "fake_mail@gmail.com"
PASSWORD = "fake_password"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_mail(self, message):
        users_info = DataManager()
        new_info = users_info.get_users_data()

        for user in new_info:
            user_mail = user["email"]

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()  # Encrypt mail
                connection.login(user=MY_MAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_MAIL,
                                    to_addrs=user_mail,
                                    msg=f"{message}".encode('utf-8'))
