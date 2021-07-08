# write by zinhyeok david9pjh@gmail.com
num = 0
while(num == 0):
    try:
        num = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        if num > 3 or num < 0:
            raise IndexError
    except ValueError:
        print('정수를 입력하세요')
        num = 0
    except IndexError:
        print('1, 2, 3 중 하나를 입력하세요')
        num = 0
