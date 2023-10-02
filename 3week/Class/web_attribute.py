import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 1. 원하는 특정 페이지에 접속하기
driver.get("https://v2-test.ohcoach.com/")
driver.implicitly_wait(15)


# 2. 임의의 엘리먼트를 선택해 get_attribute() 메소드로 속성 값을 출력하기 (있는/없는 경우 분기)
elem = driver.find_element(By.CSS_SELECTOR,"#email")

if elem.get_attribute("placeholder") == None:
    print("placeholder가 없는 엘리먼트")
else:
    print(elem.get_attribute("placeholder"))
    
    
# 3. 임의의 엘리먼트의 text를 추출하기 (있는/없는 경우 분기)
elem = driver.find_element(By.CSS_SELECTOR,"#email")

if elem.text == "":
    print("text가 없는 엘리먼트")
else:
    print(elem.text)


# 4. 임의의 엘리먼트의 location 정보를 추출하고 각 Key를 호출해 Value를 하나씩 출력하기
elem = driver.find_element(By.CSS_SELECTOR,"#email")
location_info = elem.location

print(f'x is {location_info["x"]}')
print(f'y is {location_info["y"]}')


# 5. text를 추출하는 기능을 어떤 시나리오에 사용할 수 있을까요?
# 알맞은 문구를 출력하는지 확인?

elem = driver.find_element(By.CSS_SELECTOR,"#kc-form-login > div.option-text > span > a > span")
print(elem.text)

time.sleep(5)