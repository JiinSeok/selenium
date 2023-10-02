from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#현재시간 구하기
now = time.strftime('%Y-%m-%d %Hh:%Mm')

result_pass_list = [] #PASS 한 TC ID를 넣는 리스트
result_fail_list = [] #FAIL 한 TC ID를 넣는 리스트
fail_reason_list = [] #FAIL 한 이유를 넣는 리스트
tc_count = 9

import os

if not os.path.exists("test_result"):
    os.makedirs("test_result")


#테스트 전 과정에 걸쳐 에러발생 시 에러 기록하는 try, except 문
try:
    f = open(f'test_result/{now}_test_result.txt', 'w')
    f.write(f'테스트 수행 일자 - {now}\n')

    #TC_001 CGV 홈페이지 접속
    tc_progress = 'TC_001-1'
    driver = webdriver.Chrome()
    driver.set_window_position(-200, 1080)
    driver.maximize_window()

    start_time = time.time()
    driver.get('https://www.cgv.co.kr')
    driver.implicitly_wait(10)
    end_time = time.time()

    try:
        if driver.find_element(By.CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > h1 > a > img').is_displayed():
            print('TC_001 CGV 로고 노출, 페이지 로딩 Pass.')
            
    except Exception as e:
        fail_reason = 'CGV 로고 미노출, 페이지 로딩 Fail'
        print(fail_reason)

    tc_progress = 'TC_001-2'
    loading_time = end_time - start_time
    if loading_time >= 10:
        print(f'TC_001-2 페이지 로딩 속도 Fail. >>> {loading_time} sec')
        print(fail_reason)
    else:
        fail_reason = f'TC_001-2 페이지 로딩 속도 Pass. >>> {loading_time} sec' 

    #TC_002 비유효한 영화이름 검색
    tc_progress = 'TC_001-2'
    loading_time = end_time - start_time
    if loading_time >= 10:
        fail_reason = f'TC_001-2 페이지 로딩 속도 Fail. >>> {loading_time} sec'
        print(fail_reason)
        result_fail_list.append(tc_progress)
        fail_reason_list.append(fail_reason)
    else:
        pass_reason = f'TC_001-2 페이지 로딩 속도 Pass. >>> {loading_time} sec'
        print(pass_reason)
        result_pass_list.append(tc_progress)





    tc_progress = 'TC_002'
    elem_search = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
    elem_search.click()

    if elem_search.get_attribute('placeholder') == '':
        print('TC_002 검색필드 클릭 Pass.')
    else:
        fail_reason = 'TC_002 검색필드 클릭 Fail. >>> ' + elem_search.get_attribute('placeholder')
        print(fail_reason)

    #비유효한 값 입력
    elem_search.send_keys('asdf!@#$!!')
    elem_search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    #비유효한 값 검색 결과 확인
    elem_search_result = driver.find_element(By.ID, 'search_result_re')
    if elem_search_result.text == '영화 또는 인물명을 확인 후 다시 검색해주세요!':
        print('TC_002 비유효한 검색 결과 Pass.')
    else:
        fail_reason = f'TC_002 비유효한 검색 결과 Fail. >>> {elem_search_result.text}'
        print(fail_reason)


    #TC_003 한글 영화이름 검색
    tc_progress = 'TC_003'
    elem_search = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
    elem_search.click()

    #한글 영화이름 검색
    elem_search.clear()
    elem_search.send_keys('토이스토리')
    elem_search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    #한글 영화이름 검색 결과 확인
    try:
        if driver.find_element(By.ID, 'searchMovieResult').is_displayed():
            movie_title = driver.find_element(By.CSS_SELECTOR, '#searchMovieResult > ul > li > div > strong')
            if movie_title.text == '토이 스토리 4\nAll':
                print(f'TC_003 한글 영화이름 검색 Pass >>> {movie_title.text}')
            else:
                fail_reason = f'TC_003 한글 영화이름 검색 Fail. >>> 검색된 영화 이름이 다름. {movie_title.text}'
                print(fail_reason)
    except Exception as e:
        fail_reason = f'TC_003 한글 영화이름 검색 실패.'
        print(fail_reason)

    #TC_004 영문 영화이름 검색
    tc_progress = 'TC_004'
    elem_search = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
    elem_search.click()

    #영문 영화이름 검색
    elem_search.clear()
    elem_search.send_keys('lion king')
    elem_search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    #영문 영화이름 검색 결과 확인
    try:
        if driver.find_element(By.ID, 'searchMovieResult').is_displayed():
            movie_title = driver.find_element(By.CSS_SELECTOR, '#searchMovieResult > ul > li > div > strong')
            if movie_title.text == '라이온 킹\nAll':
                print(f'TC_004 영문 영화이름 검색 Pass >>> {movie_title.text}')
            else:
                fail_reason = f'TC_004 영문 영화이름 검색 Fail. >>> 검색된 영화 이름이 다름. {movie_title.text}'
                print(fail_reason)
    except Exception as e:
        fail_reason = f'TC_004 영문 영화이름 검색 실패.'
        print(fail_reason)

    #TC_005 특수문자 영화이름 검색
    tc_progress = 'TC_005'
    elem_search = driver.find_element(By.CSS_SELECTOR, '#header_keyword')
    elem_search.click()

    #특수문자 영화이름 검색
    elem_search.clear()
    elem_search.send_keys('방가!')
    elem_search.send_keys(Keys.ENTER)
    driver.implicitly_wait(10)

    #특수문자 포함 영화이름 검색 결과 확인
    try:
        if driver.find_element(By.ID, 'searchMovieResult').is_displayed():
            movie_title = driver.find_element(By.CSS_SELECTOR, '#searchMovieResult > ul > li > div > strong')
            if movie_title.text == '방가?방가!\n12':
                print(f'TC_005 특수문자 포함 영화이름 검색 Pass >>> {movie_title.text}')
            else:
                fail_reason = f'TC_005 특수문자 포함 영화이름 검색 Fail. >>> 검색된 영화 이름이 다름. {movie_title.text}'
                print(fail_reason)
    except Exception as e:
        fail_reason = f'TC_005 특수문자 포함 영화이름 검색 실패.'
        print(fail_reason)

    #TC_006 영화 상세정보 페이지 이동
    tc_progress = 'TC_006'
    movie_poster = driver.find_element(By.CSS_SELECTOR, '#searchMovieResult > ul > li > a > img')
    movie_poster.click()
    driver.implicitly_wait(10)

    try:
        if driver.find_element(By.CSS_SELECTOR, '#menu > div.col-detail > ul').is_displayed():
            print('TC_006 영화 상세페이지 진입 Pass.')
    except Exception as e:
        fail_reason = 'TC_006 영화 상세페이지 진입 Fail.'
        print(fail_reason)

    #TC_007 CGV 로고 기능 확인
    tc_progress = 'TC_007'
    logo = driver.find_element(By. CSS_SELECTOR, '#cgvwrap > div.header > div.header_content > div > h1 > a > img')
    logo.click()
    driver.implicitly_wait(10)

    try:
        driver.find_element(By.CSS_SELECTOR, '#contaniner > div.noticeClient_wrap > div > div.noticeClient_container > div.qr_wrap > div > img').is_displayed()
        print('TC_007 CGV 로고 기능 홈으로 이동 Pass.')
    except Exception as e:
        fail_reason = 'TC_007 CGV 로고 기능 홈으로 이동 Fail.'
        print(fail_reason)

except Exception as e:
    print(f'에러 발생하여 테스트 스크립트 종료. {tc_progress} >>> {e}')


# PASS 테스트 결과 기록
f.write("\n[RESULT PASS]\n")
for pass_cnt in result_pass_list:
    f.write(f"{pass_cnt}: PASS\n")

# FAIL 테스트 결과 기록
f.write("\n[RESULT FAIL]\n")
for fail_cnt in range(len{result_fail_list}):
    f.write(f"{result_fail_list[fail_cnt]}: FAIL\n")
    f.write(f"\tFAIL REASON: {fail_reason_list[fail_cnt]}\n")

# 통계
f.write("\n")
f.write(f"PASS TC COUNT: {len(result_pass_list)}\n")
f.write(f"FAIL TC COUNT: {len(result_fail_list)}\n")
f.write(f"COMPLETED TC COUNT: ")
f.write(f"PROGRESS OF TEST: ")
f.write(f"")
f.close()

import gspread
