import requests
from bs4 import BeautifulSoup

result = requests.get("https://hckrnews.com")

print(result.status_code)

html = result.content

soup = BeautifulSoup(html, 'lxml')

links = soup.find_all("a")

print(links)
