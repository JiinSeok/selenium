#while 문을 이용해 사용자에게 'exit'를 입력받기 전까지 계속 입력받기.

users_input1 = input('입력하세요 1: ')

while(users_input1 != 'exit'):
    if users_input1 != 'exit': 
        users_input1 = input('입력하세요 1: ')
        
        
while(users_input2 := input("입력하세요 2:")):
    if users_input2 == "exit":
        break