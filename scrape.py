from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/Users/Eigenaar/AppData/Local/Google/Chrome/Application/chromedriver.exe")
driver.get("https://hckrnews.com/")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

for row in soup.find_all("li", {"class": "entry row"}):

    commentElement = row.find("span", {"class": "comments"})
    pointsElement = row.find("span", {"class": "points"})
    titleElement = row.find("a", {"class": "story", "data-date": None})

    if commentElement is not None and commentElement.text != "":
        comments = commentElement.text
        points = pointsElement.text
        title = titleElement.text
        print(comments + ", " + points + ", TITLE: " + title)

print("Start scraping hckrnews.com")
