AngelaL = int(input())
AngelaR = int(input())
DanD = int(input())
DanU = int(input())

if AngelaL == DanD and AngelaR == DanU:
    print("EMPTY")
elif AngelaL < 0 and AngelaR > 0 and DanD > 0 and DanU > 0:
    print('ZERO')
elif AngelaL < 0 and AngelaR > 0 and DanU < 0 and DanD < 0:
    print('ZERO')
elif AngelaL >= DanU or AngelaR <= DanD:
    print("ZERO")
elif AngelaL < 0 and AngelaL % 2 == 1:
    print("NEGATIVE")
elif AngelaR > DanU or AngelaL > DanD and AngelaL % 2 == 0:
    print("POSITIVE")



