from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/Users/Eigenaar/AppData/Local/Google/Chrome/Application/chromedriver.exe")
driver.get("https://hckrnews.com/")

print("Start scraping hckrnews.com")
