import smtplib
import ssl
import os
from dotenv import load_dotenv
load_dotenv()
password = os.getenv("PASSWORD")
email = os.getenv("EMAIL")
receiver = os.getenv("RECEIVER")

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user = email
    password = password
    receiver = receiver
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        # The SMTP_SSL has multiple arguments that are in order so there is need to specify argument.
        server.login(user, password)
        server.sendmail(user, receiver, message)
