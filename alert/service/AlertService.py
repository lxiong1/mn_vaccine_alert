import os
import smtplib
import sys
import textwrap
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from icecream import ic

ic.configureOutput(includeContext=True)


class AlertService:
    def __init__(self, available_appointments):
        self._available_appointments = available_appointments

    def send_text_alert(self):
        try:
            email_address = os.environ.get("EMAIL")
            password = os.environ.get("EMAIL_PASSWORD")
            phone_number = os.environ.get("PHONE_NUMBER")
            sms_gateway = f"{phone_number}@tmomail.net"

            ic(f"Sending SMS message to {phone_number}")

            sms_message = MIMEMultipart()
            sms_message["From"] = email_address
            sms_message["To"] = sms_gateway
            sms_message["Subject"] = f"Available MN Vaccine Apointments"

            text_message = self.__create_text_message()
            if text_message:
                sms_message.attach(MIMEText(text_message, "plain",))

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(email_address, password)
                server.sendmail(email_address, sms_gateway, sms_message.as_string())

                ic(f"Successfully sent SMS message to {phone_number}")

                server.quit()
        except:
            ic(traceback.print_exc())
            sys.exit()

    def __create_text_message(self):
        if self._available_appointments:
            text_message = ""

            for appointment in self._available_appointments:
                message = f"""
                Appointments at {appointment["provider"].upper()}
                Location: {appointment["location"]}
                Sign up here: {appointment["url"]}
                    
                """

                text_message += message

            return textwrap.dedent(text_message)
        else:
            ic("No MN vaccine appointment is available")
            return None
