players = int(input())
count = 0
if 1 <= players <= 10000:
    for player in range(players):
        points = int(input())
        fouls = int(input())
        player = (points * 5) - (fouls * 3)
        if player > 40:
            count = count + 1

    if count == players:
        print(str(count) + '+')
    else:
        print(count)

