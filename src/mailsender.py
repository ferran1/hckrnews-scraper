import smtplib
import keyring
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email = "ferrantl@live.nl"
password = keyring.get_password(service_name="mail_app", username="ferrantl")

# set up SMTP server
s = smtplib.SMTP('smtp-mail.outlook.com', port=587)
s.starttls()
s.login(email, password)


def send_mail(title, url):
    msg = MIMEMultipart()  
    message = url

    # setup the parameters of the message
    msg['From'] = email
    msg['To'] = email
    msg['Subject'] = title

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)
