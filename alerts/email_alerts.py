# email_alerts.py
# Mike Bell
# 05/21/2026

import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(subject, body):
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = EMAIL_ADDRESS
    message["To"] = EMAIL_ADDRESS

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)