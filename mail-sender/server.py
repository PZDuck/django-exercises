import threading
import smtplib, ssl
import random, time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

messages = []

port = 587
sender_email = os.environ.get("EMAIL")
receiver_email = input("Please enter your email: ")
password = os.environ.get("PASSWORD")

context = ssl.create_default_context()

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test"

text = "This is a new test message"

message.attach(MIMEText(text, "plain"))

class EmailSender(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        time.sleep(10)
        messages.append(message)

        with smtplib.SMTP(os.environ.get("SMTP"), port) as server:
            print("Sending email...")
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    thread1 = EmailSender()
    thread2 = EmailSender()
    thread3 = EmailSender()