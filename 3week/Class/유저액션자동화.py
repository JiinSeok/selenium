import time
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains as AC

driver = webdriver.Chrome()

# 클릭
driver.get("https://www.cgv.co.kr/")

elem = driver.find_element(By.CSS_SELECTOR,"#header_keyword").click()

time.sleep(3)


# 클릭하고 입력하고 검색
driver.get("https://www.cgv.co.kr/")

elem = driver.find_element(By.CSS_SELECTOR,"#header_keyword")
elem.click()
elem.send_keys("노아 바움백")
time.sleep(1)

elem.clear()
time.sleep(1)

elem.send_keys("그레타 거윅")
driver.find_element(By.CSS_SELECTOR,"#btn_header_search").click()
time.sleep(1)

driver.execute_script("window.scrollTo(0,100)")
time.sleep(1)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(1)

actions = AC(driver)
actions.perform()