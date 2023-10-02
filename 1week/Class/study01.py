a = 5
print(a)

a = 8
print(a)

a = 5
b = 3
print(a+b)

a = 8
b = 3
print(f'a+b = {a+b}')

a = 5
b = 3
c = a+b
print(c)

print(f'저는 {26}세입니다.')

# 문장 안에 ' 따옴표를 쓰고 싶다면 앞에 역 슬래시 \를 붙여서 사용!
print(f'I\'m your bunny that you hold tight when you go to sleep')

age = 26
name = 'Jiin Seok'

print(f'My name is {name}, I\'m {age} years old.')

# 0으로 나누면 에러

# 몫 구하기 //

# 나머지 구하기 % --> 홀/짝 구별에 사용

a = 6 % 2
print(a)

a = 7
b = 2
print(a%b)

# 연산의 우선순위
# 괄호를 씌우면 우선 연산

# +로 문자열 합치기
s1 = '오늘 저녁은'
s2 = '지인이'
s3 = '혼자'

print(s1 + s2 + s3)
print(f'{s1} {s2} {s3}')

# int 정수
# float 실수
# str 문자열
# list 리스트
# tuple 튜플
# dictionaries 딕셔너리

# 동일 자료형 간의 연산 => 가능

# 상이 자료형 간의 연산 => 에러
a = '5'
b = 3
# 형변환: 데이터의 자료형을 임의로 변환해 사용하는 것
print(int(a) + b)

a = '5'
b = 3
print(int(a) + b)
print(a + str(b))

# 형변환을 해도 변수 자체의 자료형이 변하지는 않는다.
print(type(a))
print(type(b))


# [대괄호]로 적는 리스트 (0번째부터 시작하는 변수의 배열)
a = [1, 3, 5]
print(a)
print(a[0])
print(type(a))

# 빈 리스트와 .append로 덧붙이기
list = []
print(list)

list.append(1)
print(list)

list.append(2)
print(list)


# .insert로 위치 지정하여 삽입
insert = [2, 4, 6, 8]
insert.insert(1,0)
print(insert)

insert[0] = 0
print(insert)


# {중괄호}로 적는 딕셔너리
TY = {'name':'태영', 'nickname':'기린', 'lover':' ', 'bad_feelings':'ㅠㅠ'}
print(TY)

TY['lover'] = '지인'
TY['good_feelings'] = '❤️'
del TY['bad_feelings']
print(TY)

print(TY['name'] + TY['good_feelings'] * 5 + TY['lover'])

# 조건문
# if {조건식} :
#   명령

# 들여쓰기가 필요한 조건문 (:)
# if {}:    
# for a in range():
# while(True):
# def sum(a,b):


a = 20

if a > 10:
    print('a는 10보다 크다')
    
if a < 10:
    print('a는 10보다 작다')


# 문자열로 입력 받기
# else if = elif
사랑한지 = input('오늘은 며칠째인가요?: ')
if int(사랑한지) % 2 == 0:
    print('사랑한지 짝수일째입니다.')

elif int(사랑한지) % 2 == 1:
    print('사랑한지 홀수일째입니다.')

else:
    print('다시 입력해 주세요.')
    

# 반복문
# 조건식이 True이면 명령문을 반복한다.
cnt = 0

while(cnt < 10):
    print(f'{cnt+1}번째 반복')
    cnt += 1
    

flag = 0
cnt = 179

while(flag == 0):
    if cnt == 200:
        flag = 1
    else:
        print(f'오늘은 {cnt+1}일!')
        cnt += 1
        

# for 변수 in range (시작값, 끝값, 연속값의차):  --- 연속값의 차 생략하면 1
#   명령어

for date in range(179,200,7):
    print(date)
    
for countdown in range(5,0,-1):
    print(countdown)


l1 = [1,2,3,4,5]
for i in range(0,5,1):
    print(l1[i])
    
    
# 향상된 for문 (통째로 출력하기)
l2 = [6,7,8,9,10]
for i in l2:
    print(i)
    
for i in range(len(l2)):
    print(l2(i))
    

# break
for date in range (179,200):
    if date == 200:
        print('200일이 되었습니다.')
        break # 자신이 속해있는 가장 가까운 반복문 종료
    else:
        print(date)
        

# continue
for date in range(179,200):
    if date % 2 == 1:
        continue # 아래 있는 코드블럭 실행 없이 다시 반복문으로 돌아감.
    print(date)
    
    
    