#예외처리
#1 
list = {0,1,2,3}
try:
    print(list[5])
except Exception as e:
    print(len(list)-1)
    

#2 
a = 1
b = "1"
try:
    print(a + b)
    
except Exception as e:
    print(int(a) + int(b))
    

#셀레니움 웹드라이버 활용

#1
# from selenium import webdriver
# driver = webdriver.Chrome()
# time.sleep(5)

#2
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.set_window_position(0,0)
#time.sleep(3)
driver.set_window_size(500,500)
time.sleep(2)
#driver.maximize_window()
#time.sleep(3)

driver.get("https://www.joongang.co.kr/article/25187952#home")
time.sleep(2)
print(driver.title)
print(driver.current_url)

driver.refresh()
driver.back()
driver.forward()
driver.quit()


# 3강
import requests
from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.minimize_window()
