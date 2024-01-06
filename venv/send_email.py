import smtplib
import ssl
import os
from dotenv import load_dotenv
load_dotenv()
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    try:
        with smtplib.SMTP_SSL(host, port) as server:
            server.login(email_user, email_password)
            server.sendmail(email_user, email_receiver, message)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")


email_user = os.getenv("EMAIL")
email_password = os.getenv("PASSWORD")
email_receiver = os.getenv("RECEIVER")


