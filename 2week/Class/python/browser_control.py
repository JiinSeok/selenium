import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.joongang.co.kr/article/25187952#home")

print(driver.title)
print(driver.current_url)

driver.set_window_position(0,0)
driver.set_window_size(800,500)\

time.sleep(3)

driver.get("https://www.joongang.co.kr")
print(driver.title)
print(driver.current_url)

driver.back()
time.sleep(3)

driver.forward()

time.sleep(3)