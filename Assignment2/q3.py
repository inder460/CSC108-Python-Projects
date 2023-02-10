class_size = input().split()

for i in range(len(class_size)):
    class_size[i] = int(class_size[i])

class_seating = []
class_row = []
class_col = []
events = []
for i in range(class_size[0]):
    seating = input().split()
    class_row.append(seating)

for i in range(class_size[0]):

    class_col = []

    for j in range(class_size[1]):
        class_col = []

        for let in class_row[i][0]:
            class_col.append(let)
    class_seating.append(class_col)

class_input_number = int(input())

for i in range(class_input_number):
    class_input = input().split()
    count = 0
    people = int(class_input[1])
    if class_input[0] == "in":
        temp = class_seating[0][:]
        count = 0
        people = int(class_input[1])
        index=0
        index2=0
        for i in range(class_size[0]):
            count=0
            temp = class_seating[i][:]
            for j in range(class_size[1]):
                if temp[j] == '1':
                    count = 0
                    temp = class_seating[i][:]

                if temp[j] == '0':
                    count = count + 1

                    temp[j] = '1'

                if count == people:
                    index = i

                    index2= j-count+1
                    break

            if count == people:
                break
            temp = class_seating[i][:]

    if count == people:
        class_seating[index] = temp
        events.append((str(index+1)+" "+str(index2+1)))

    elif class_input[0] == "out":
        class_seating[int(class_input[1])-1][int(class_input[2])-1]='0'

    else:
        events.append('-1')

for i in range(len(events)):
    print()
    for j in range(len(events[i])):
        print(events[i][j], end='')
for i in range(len(class_seating)):
    print()
    for j in range(len(class_seating[i])):
        print(class_seating[i][j], end='')