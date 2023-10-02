import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# CLASS_NAME
driver.get("https://v2-test.ohcoach.com/")
driver.implicitly_wait(15)
driver.find_element(By.CLASS_NAME,"option-text").click()
time.sleep(3)

# ID
driver.get("https://v2-test.ohcoach.com/")
driver.implicitly_wait(15)
driver.find_element(By.ID,"kc-login").click()
time.sleep(3)

# XPATH
driver.get("https://v2-test.ohcoach.com/")
driver.implicitly_wait(15)
driver.find_element(By.XPATH,'//*[@id="kc-form-login"]/div[4]/span/a/span').click()
time.sleep(3)

# CSS_SELECTOR
driver.get("https://v2-test.ohcoach.com/")
driver.implicitly_wait(15)
driver.find_element(By.CSS_SELECTOR,"#kc-login").click()
time.sleep(3)

