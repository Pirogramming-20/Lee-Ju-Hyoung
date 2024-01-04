num = 0

while True: 
    getnum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
    if not getnum.isdigit():
        print('정수를 입력하세요')
    elif int(getnum) > 3 or int(getnum) < 0:
        print('1, 2, 3 중 하나를 입력하세요')
    
    else:
        break
    