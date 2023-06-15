import requests
from dotenv import load_dotenv
import os


# This code is to send emails to recipients in the fornat
# send_email("to", "subject", "content")

def send_email(to, subject, content):
    """ This method sends an email to the given email address 
        subject: Subject of the email
        content: Content of the email
        to: Email address to send the email
    """

    URL = os.getenv("ACTIVEPIECES_MAILER_ENDPOINT")

    data = {
        "subject": subject,
        "content": content,
        "to": to
    }

    response = requests.post(URL, json=data)
    return response.status_code