import time
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.get("https://www.naver.com")

# 10초간 페이지 로드를 기다린다 (묵시적 대기)
driver.implicitly_wait(5)

# 인스펙터 검사 결과
# <a href="https://nid.naver.com/nidlogin.login?mode=form&amp;url=https://www.naver.com/" class="MyView-module__link_login___HpHMW"><i class="MyView-module__naver_logo____Y442"><span class="blind">NAVER</span></i>로그인</a>

# find_element() 메소드에 인스펙터로 검사한 요소(엘리먼트)의 정보를 매개변수로 변겨 요소를 지정한다.
# By 지정자: 요소를 찾을 속성을 지정하는 명령어 - CSS_SELECTOR, CLASS_NAME, ID, XPATH
# click() 메소드로 좌클릭 수행한다.
driver.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW").click()

# 무조건 대기
time.sleep(3)


# driver.find_element(By.CLASS_NAME,"")
driver.get("https://www.cgv.co.kr")
driver.implicitly_wait(15)
driver.find_element(By.CLASS_NAME,"btn_totalSearch").click()
time.sleep(5)


# driver.find_element(By.ID,"")
driver.get("https://www.naver.com")
driver.implicitly_wait(10)
driver.find_element(By.ID,"search-btn").click()
time.sleep(5)


# driver.find_element(By.XPATH,"")
# XPATH: XML 문서의 구조를 검색하는 쿼리. HTML 문서에서 엘리먼트 검색, 식별할 수 있다.
driver.get("https://www.cgv.co.kr")
driver.implicitly_wait(15)
driver.find_element(By.XPATH,'//*[@id="btn_allView_Movie"]').click()
time.sleep(5)


# driver.find_element(By.CSS_SELECTOR,"")
# css의 규칙을 적용할 요소를 지정, xpath보다 지정 속도가 빠르다.
driver.get("https://www.cgv.co.kr")
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,"#btn_allView_Movie").click()
time.sleep(5)

# 웹 엘리먼트 속성 다루기
driver.get("https://www.cgv.co.kr")
driver.implicitly_wait(10)

elem = driver.find_element(By.CSS_SELECTOR,"#btn_allView_Movie")

href = elem.get_attribute("href")
src = elem.get_attribute("src")

# 속성을 찾을 수 없으면 None을 반환
print(elem.get_attribute("qwerty"))

if elem.get_attribute("qwerty") == None:
    print("qwerty 속성이 없는 엘리먼트")
    
else:
    print(elem.get_attribute("qwerty"))
    
# text
elem = driver.find_element(By.CSS_SELECTOR,"#btn_allView_Movie")

# 이때 문자열 데이터가 없는 엘리먼트는 아무 결과도 반환하지 않는다.
print(elem.text)

if elem.text == "":
    print("text가 없는 엘리먼트")
else:
    print(elem.text)

# text로 입력되어야 할 문자열의 상태 검증
origin_text = "로그인하기"

if origin_text == elem.text:
    test_result = "pass"
elif origin_text != elem.text:
    test_result = "fail"
    print(elem.text)


# location
elem = driver.find_element(By.CSS_SELECTOR,"#btn_allView_Movie")
print(elem.location)

# 좌표는 딕셔너리 자료형이므로 Key 값으로 Value에 접근해 데이터를 활용할 수 있다.
location_info = elem.location
print(location_info["x"])

# size
elem = driver.find_element(By.CSS_SELECTOR,"#btn_allView_Movie")
print(elem.size)

size_info = elem.size

if size_info["height"] < size_info["width"]:
    print("가로로 길다.")
elif size_info["height"] > size_info["width"]:
    print("세로로 길다.")
    

# 무조건 대기: 페이지 로드하지 못해도 오류 발생 X -> 페이지 로드 후 대기
driver.get("https://news.zum.com")
time.sleep(10)
print("10초 대기 완료!")

# 묵시적 대기: 페이지 로드 실패하면 오류 발생, 코드 종료
driver.get("https://news.zum.com")
driver.implicitly_wait(10)
print("10초까지 대기 완료!")

# 명시적 대기: 지정한 엘리먼트가 로드될 때까지 기다려 찾아라
driver.get("http://www.cgv.co.kr")

try:
    elem = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,"#btn_allView_Movie"))
    )
    elem = driver.find_element(By.CSS_SELECTOR,"#btn_allView_Movie")
    print(elem.get_attribute("href"))

except Exception as e:
    print(f'{e}')


# 1. 원하는 특정 페이지 접속
driver.get("https://www.myhome.go.kr/")
driver.implicitly_wait(10)
# 2. 묵시적 대기로 페이지 로딩 기다리기


# 3. 임의 엘리먼트 지정해 원하는 속성 출력
elem1 = driver.find_element((By.CSS_SELECTOR,'#myhome-potal > div.potal-wrap > div:nth-child(2) > a > h2'))
print(elem1.get_attribute("title"))

# 4. 다른 페이지로 이동하여 명시적 대기로 임의 엘리먼트의 속성 출력
driver.get("https://www.myhome.go.kr/hws/portal/main/getMgtMainYhsPage.do")

try:
    elem2 = WebDriverWait(driver,10).until(
        EC.presence_of_element_located(By.CSS_SELECTOR,"#myhome-main > header > div > a.img-logo > img")
    )
    elem2 = driver.find_element(By.CSS_SELECTOR,"##myhome-main > header > div > a.img-logo > img")
    print(elem2.get_attribute("src"))

except Exception as e:
    print(f'{e}')

# 5. 코드가 끝난 뒤 브라우저가 n초간 꺼지지 않도록 time.sleep()으로 코드 진행을 멈추기

time.sleep(5)


