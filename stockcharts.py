from typing import KeysView
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import urllib.request

driver = webdriver.Chrome()
driver.get("https://stockcharts.com/")

symbols = ['spy', 'appl', 'msft', 'goog']
count = 1
for i in symbols:

    t = driver.find_elememt_by_id("nav-chartSearch-input").send_keys(i)

    driver.implicity_wait(2)
    imgUrl = driver.find_element_by_css_selector(".chartImg").get_attribute(i)

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
    count = count + 1
    driver.back()
