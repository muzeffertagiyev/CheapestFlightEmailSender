import smtplib
import os

MY_EMAIL = os.environ['EMAIL']
EMAIL_PASSWORD = os.environ['PASSWORD']


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def sending_email(self, emails, google_flight_link, message):
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
            for email in emails:
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=f'{email}', msg=f"Subject:Cheapest Flights\n\n"
                                                                                 f"{message}\n{google_flight_link}".encode("utf-8"))
            print("Email was sent successfully")
