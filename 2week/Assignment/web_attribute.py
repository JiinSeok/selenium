#1. Selenium과 Python을 이용해 임의의 페이지 5개에 접근하기.
#2. 접근한 페이지들의 타이틀을 title = [] 리스트에 추가하기.
#3. 접근한 페이지들의 URL을 url = [] 리스트에 추가하기.
#4. title 리스트와 url 리스트를 출력하기.

import time
from selenium import webdriver

driver = webdriver.Chrome()

title = []
url = []

driver.get("https://edu.ggwf.or.kr/")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://comento.kr/")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://ylaccount.kinfa.or.kr/")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://yozm.wishket.com/magazine/detail/1438/")
title.append(driver.title)
url.append(driver.current_url)

driver.get("https://insight.wanted.co.kr/")
title.append(driver.title)
url.append(driver.current_url)

print(title)
print(url)


#모듈화를 배워보자

urls = ["https://edu.ggwf.or.kr/","https://comento.kr/", "https://ylaccount.kinfa.or.kr/"]

class CrowlerInfo:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.titles = list()
        self.urls = list()

    def visit(self, url):
        self.driver.get(url)
        self._add_title(self.driver.title)
        self._add_url(self.driver.current_url)
        

    def _add_title(self, title: str):
        self.titles.append(title)
    
    def _add_url(self, url: str):
        self.urls.append(url)

    def print(self):
        print(self.titles)
        print(self.urls)

crawler = CrowlerInfo()

for url in urls:
    crawler.visit(url)

crawler.print()