num = 0
count = 1

while True: 
    getnumA = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
    if not getnumA.isdigit():
        print('정수를 입력하세요')
    elif int(getnumA) > 3 or int(getnumA) < 0:
        print('1, 2, 3 중 하나를 입력하세요')
    else:
        break
for i in range(int(getnumA)):
    print('playerA :', count)
    count+=1