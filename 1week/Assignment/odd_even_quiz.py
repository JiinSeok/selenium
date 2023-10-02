#입력받은 정수가 홀수인지 짝수인지 판별하여 결과를 출력하기.

number = int(input('정수를 입력하세요.: '))

if number %2 == 0:
    print('짝수입니다.')

elif number %2 == 1:
    print('홀수입니다.')