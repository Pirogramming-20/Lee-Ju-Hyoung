num = 0
count = 1
flag = 0

def brGame(flag):
    num = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
    if not num.isdigit():
        print('정수를 입력하세요')
        return flag, 0
    elif int(num) > 3 or int(num) < 0:
        print('1, 2, 3 중 하나를 입력하세요')
        return flag, 0
    else:
        flag=abs(flag-1)
        return flag, int(num)

while True:
    while flag==0: 
        flag, num = brGame(flag)
        for i in range(int(num)):
            print('playerA :', count)
            count+=1
            if count > 31:
                print('playerB win!')
                exit()
    while flag==1: 
        flag, num = brGame(flag)
        for i in range(int(num)):
            print('playerB :', count)
            count+=1
            if count > 31:
                print('playerA win!')
                exit()