my_account = float(input())
min_balance = float(input())

if my_account >= 100000.00:
    rich = True
    close = False
    print(rich)
    print(close)
elif my_account >= min_balance:
    if my_account-min_balance > 30:
        close = False
        print(close)
    elif my_account-min_balance <= 30:
        close = True
        print(close)

