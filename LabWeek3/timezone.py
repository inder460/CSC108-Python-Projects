TorontoTime = float(input())
TorDayLight = int(input())
LonDayLight = int(input())

if TorDayLight == 1 and LonDayLight == 1:
    LondonTime = TorontoTime + 6.0
    if LondonTime > 24.0:
        LondonTime = LondonTime - 24.0
        print(LondonTime)
    else:
        print(LondonTime)

elif TorDayLight == 1 and LonDayLight == 0:
    LondonTime = TorontoTime + 5.0
    if LondonTime > 24.0:
        LondonTime = LondonTime - 24.0
        print(LondonTime)
    else:
        print(LondonTime)

elif TorDayLight == 0 and LonDayLight == 1:
    LondonTime = TorontoTime + 7.0
    if LondonTime > 24.0:
        LondonTime = LondonTime - 24.0
        print(LondonTime)
    else:
        print(LondonTime)