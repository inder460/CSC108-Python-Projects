# prompt for trainee identifier
digit1 = int(input())
digit2 = int(input())
digit3 = int(input())
digit4 = int(input())
digit5 = int(input())

if digit2 > digit1 + 1 or digit2 < digit1 - 1 or digit2 == digit1:
    print('INVALID')
elif digit2 == digit1 + 1 or digit2 == digit1 - 1:
    if digit3 > digit2 + 1 or digit3 < digit2 - 1 or digit3 == digit2:
        print('INVALID')
    elif digit3 == digit2 + 1 or digit3 == digit2 - 1:
        if digit4 > digit3 + 1 or digit4 < digit3 - 1 or digit4 == digit3:
            print('INVALID')
        elif digit4 == digit3 + 1 or digit4 == digit3 - 1:
            if digit5 > digit4 + 1 or digit5 < digit4 - 1 or digit5 == digit4:
                print('INVALID')
            elif digit5 == digit4 + 1 or digit5 == digit4 - 1:
                print('VALID')




