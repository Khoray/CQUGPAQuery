import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as bs
import re

# 一下三行为无头模式运行，无头模式不开启浏览器，也就是在程序里面运行的
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(executable_path=(r'chromedriver.exe'), options=chrome_options)
# #如果不用上面三行，那么就用下面这一行。运行的时候回自动的开启浏览器，并在浏览器中自动运行，你可以看到自动运行的过程
# browser = webdriver.Chrome(executable_path=(r'chromedriver.exe'))
# 设置访问链接
browser.get("http://oldjw.cqu.edu.cn:8088/")
# 输入用户名和密码
browser.find_element_by_name("username").send_keys(input("username(学号):"))
browser.find_element_by_name("password").send_keys(input("password(身份证后六位):"))
# 点击登录按钮

browser.find_element_by_name("submit1").click()

# 获取cookie
cookie_items = browser.get_cookies()
cookie_str = ""
# 组装cookie字符串
for item_cookie in cookie_items:
    item_str = item_cookie["name"]+"="+item_cookie["value"]+"; "
    cookie_str += item_str

url = 'http://oldjw.cqu.edu.cn:8088/score/sel_score/sum_score_sel.asp'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": cookie_str,
    "Host": "oldjw.cqu.edu.cn:8088",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.64"
}

response = requests.get(url = url, headers = headers)

response.encoding = 'gb2312'
html = response.content

with open("test.txt", "w") as f:
    f.write(response.text)



content = response.text
soup = bs(content)

# print(soup.prettify())

kemu = soup.find_all('table')[0].find_all("tr")[1].find_all("td")[0].find_all("table")[0].find_all("tr")

for i in kemu:
    lst = i.find_all("td")
    lst = [j.get_text().replace("\n", "").strip() for j in lst]
    print("{0:20s}{1:20s}{2:20s}".format(lst[2], lst[3], lst[4]))


GPA = re.findall("<B>GPA：</B>(.*)</B>", content)
print("平均绩点:", GPA[0])