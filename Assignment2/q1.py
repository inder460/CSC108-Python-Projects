students_events = input().split()

for i in range(len(students_events)):
    students_events[i] = int(students_events[i])

group = input().split()

eventCount = 0
teamA = 0
teamB = 0
while eventCount < students_events[1]:

    eventType = input().split()
    eventCount = eventCount + 1

    if eventType[0] == 'cite':
        eventType.pop(0)
        for i in range(len(eventType)):
            eventType[i] = int(eventType[i])

        x = eventType.pop(0)
        y = eventType.pop(0)

        cite = [group[x-1], group[y-1]]
        if cite[0] == 'A' and cite[1] == 'A':
            teamA = teamA + 1
        elif cite[0] == 'A' and cite[1] == 'B':
            teamB = teamB + 5
        elif cite[0] == 'B' and cite[1] == 'A':
            teamA = teamA + 5
        elif cite[0] == 'B' and cite[1] == 'B':
            teamB = teamB + 1

    elif eventType[0] == 'change':
        eventType.pop(0)
        for i in range(len(eventType)):
            eventType[i] = int(eventType[i])
        studentChange = eventType.pop(0)
        if group[studentChange-1] == 'A':
            group[studentChange - 1] = 'B'
        elif group[studentChange-1] == 'B':
            group[studentChange - 1] = 'A'

print(teamA, teamB)