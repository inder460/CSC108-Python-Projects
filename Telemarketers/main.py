# prompt user to enter each digit of their number
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

# check if inputted numbers satisfy the conditions needed
# if first digit 8 or 9, fourth digit 8 or 9,
# second and third digit same, print ignore
if ((num1 == 8 or num1 == 9)
        and (num4 == 8 or num4 == 9)
        and (num2 == num3)):
    print('ignore')
# else print answer
else:
    print('answer')
