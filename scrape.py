import requests
from bs4 import BeautifulSoup

result = requests.get("https://hckrnews.com")

result_status = result.status_code

html = result.content

soup = BeautifulSoup(html, 'lxml')


# artciles which are declared DEAD have a 'dead' value in the class attribute
# return False if article is declared DEAD else True
def is_not_dead(element):
    return 'dead' not in element['class']


articles = soup.find_all("a", class_="link span15 story")

# Keywords to look for in the titles
keywords = ["Ubuntu", "Microservices", "Encryption", "Academia"]

for article in articles:
    for keyword in keywords:
        if keyword in article.text:
            title = article.text
            url = article.attrs['href']
            if title and url is not None \
                    and is_not_dead(title):
                print(title)
                print(url)
                # Send mail
