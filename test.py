import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
import re

content = ""

with open("test.txt", "r") as f:
    content = f.read()

soup = bs(content)

# print(soup.prettify())

kemu = soup.find_all('table')[0].find_all("tr")[1].find_all("td")[0].find_all("table")[0].find_all("tr")

for i in kemu:
    lst = i.find_all("td")
    lst = [j.get_text().replace("\n", "").strip() for j in lst]
    print("{0:20s}{1:20s}{2:20s}".format(lst[2], lst[3], lst[4]))


GPA = re.findall("<B>GPA：</B>(.*)</B>", content)
print("平均绩点:", GPA[0])