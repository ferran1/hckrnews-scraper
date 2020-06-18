import requests
from bs4 import BeautifulSoup

result = requests.get("https://hckrnews.com")

result_status = result.status_code

html = result.content

soup = BeautifulSoup(html, 'lxml')


def is_not_dead(element):
    return 'dead' not in element['class']


for row in soup.find_all("li", class_="entry row"):

    comment_element = row.find("span", class_="comments")
    points_element = row.find("span", class_="points")
    title_element = row.find("a", {"class": "story", "data-date": None})

    if comment_element and points_element and title_element is not None \
            and is_not_dead(title_element):
        comments = comment_element.text
        points = points_element.text
        title = title_element.text
        link = title_element["href"]
