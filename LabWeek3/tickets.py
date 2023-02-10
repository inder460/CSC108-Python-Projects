regNum = int(input())
stuNum = int(input())
holiday = int(input())

ticketNum = regNum + stuNum
regular = regNum * 3.99
student = stuNum * 2.99
if ticketNum >= 10:
    if holiday == 1:
        price = (regular+student) * 0.95
        print(price)
    elif holiday == 0:
        price = (regular + student) * 0.90
        print(price)
elif ticketNum < 10:
    price = regular + student
    print(price)