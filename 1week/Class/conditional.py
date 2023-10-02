age = int(input('나이: '))

if age >= 20:
    print('성인')
    
if age < 20:
    print('미성년자')

    
score = int(input('점수: '))

if score >= 90:
   grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score < 60:
    grade = 'F'

print(f'{grade}학점')
    

list10 = [1,2,3,4,5,6,7,8,9,10]
index = int(input('인덱스: '))
if index % 2 == 0:
    print('짝수')
    
elif index % 2 == 1:
    print('홀수')