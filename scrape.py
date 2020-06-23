import requests
from bs4 import BeautifulSoup

# import for Mail purposes
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ['GMAIL_EMAIL']
EMAIL_PASSWORD = os.environ.get('GMAIL_PASSWORD_PYTHON_TEST')
print(EMAIL_ADDRESS)
print(EMAIL_PASSWORD)

contacts = ['zorabdul@gmail.com', 'ferran1004@gmail.com ']

result = requests.get("https://hckrnews.com")

result_status = result.status_code

html = result.content

soup = BeautifulSoup(html, 'lxml')


# Sends e-mail with array of html string
def send_email(articles_html: []):
    msg = EmailMessage()
    msg['Subject'] = 'News from hckernews! '
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    # msg['To'] = ", ".join(contacts)

    msg.add_alternative("<br>".join(articles_html), subtype="html")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


# artciles which are declared DEAD have a 'dead' value in the class attribute
# return False if article is declared DEAD else True
def is_not_dead(element):
    return 'dead' not in element['class']


articles = soup.find_all("a", class_="link span15 story")

# Keywords to look for in the titles
keywords = ["Ubuntu", "Microservices", "Encryption", "Academia", "Jira", "RSS"]

found_articles = []

for article in articles:
    for keyword in keywords:
        if keyword in article.text:
            title = article.text
            url = article.attrs['href']

            if title and url is not None \
                    and is_not_dead(article):
                found_articles.append(str(article))
                print(found_articles)

# Send mail
send_email(found_articles)
