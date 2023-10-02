#1~10 사이의 정수를 입력받아 해당 구구단 단을 출력하기.

one_to_ten = int(input('1부터 10 사이의 정수를 입력하세요.: '))

for i in range(1,10):
    print(f'{one_to_ten} x {i} = {one_to_ten * i}')