halfM = float(input())
hilly = int(input())

marathonTime = halfM * 2

if hilly == 1:
    marathonTime = marathonTime + 20.0
    print(marathonTime)
elif hilly == 0:
    marathonTime = marathonTime + 10.0
    print(marathonTime)