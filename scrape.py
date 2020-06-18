import requests
from bs4 import BeautifulSoup

result = requests.get("https://hckrnews.com")

print(result.status_code)

html = result.content

soup = BeautifulSoup(html, 'lxml')

articles = soup.find_all("a", class_="link span15 story")

# Keywords to look for in the titles
keywords = ["Ubuntu", "Microservices", "Encryption", "Academia"]

articles_found = []

for article in articles:
    for keyword in keywords:
        if keyword in article.text:
            articles_found.append([article.text, article.attrs['href']])

# print(articles)
print(articles_found)
