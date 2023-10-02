import time
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

# 무조건 대기: 페이지 로드하지 못해도 오류 발생 X -> 페이지 로드 후 대기
driver.get("https://news.zum.com")
time.sleep(5)
print("5초 대기 완료!")

# 묵시적 대기: 페이지 로드 실패하면 오류 발생, 코드 종료
driver.get("https://news.zum.com")
driver.implicitly_wait(10)
print("10초까지 대기 완료!")



# 명시적 대기: 지정한 엘리먼트가 로드될 때까지 기다려 찾아라

# 1. 원하는 특정 페이지 접속
driver.get("https://news.zum.com")

# 2. 묵시적 대기로 페이지 로딩 기다리기
driver.implicitly_wait(10)

# 3. 임의 엘리먼트 지정해 원하는 속성 출력
elem1 = driver.find_element(By.XPATH,'//*[@id="container"]/section[1]/div/h1')
print(elem1.text)

# 4. 다른 페이지로 이동하여 명시적 대기로 임의 엘리먼트의 속성 출력
driver.get("https://zum.com/")

try:
    elem2 = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#search-input"))
    )
    elem2 = driver.find_element(By.CSS_SELECTOR,"#search-input")
    print(elem2.get_attribute("placeholder"))

except Exception as e:
    print(f'{e}')
    

DK