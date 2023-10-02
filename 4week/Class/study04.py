import os

if not os.path.exists("태영"):
    os.makedirs("태영")

f = open("./태영이에게.txt","w")
f.write("태영아 안녕")

f = open("./태영이에게.txt","a")
f.write("\n200일에 봐서 기뻐")

f.close()


import time
import pyautogui
from selenium import webdriver

pyautogui.screenshot("./img_search/1.png",region=(0,0,1920,1080))

mouse_position = pyautogui.position()
print(mouse_position)

# 결과 (튜플)
# Point(x=1452, y=361)

print(mouse_position[0])
print(mouse_position[1])

driver = webdriver.Chrome()

driver.get("https://www.cgv.co.kr")
driver.implicitly_wait(10)
pyautogui.click()
pyautogui.click(578,416)
pyautogui.click(button='right')
pyautogui.doubleClick()
time.sleep(3)

driver.get("https://www.cgv.co.kr")
driver.implicitly_wait(10)
pyautogui.click(948,418)
pyautogui.typewrite("movie")
pyautogui.click(1084,416)
time.sleep(4)

# driver.get("https://www.cgv.co.kr")
# driver.implicitly_wait(10)
# pyautogui.keyDown('ctrl')
# pyautogui.press('a')
# pyautogui.keyUp('ctrl')
# time.sleep(2)


# 윈도우 사이즈, 포지션은 고정해야 클릭 좌표를 반복해서 쓸 수 있다.