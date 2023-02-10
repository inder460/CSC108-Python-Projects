instruction = input()
last_instruction = ''

while instruction != '99999':
    sum = int(instruction[0]) + int(instruction[1])
    steps = instruction[2:]

    if sum%2 == 1:
        last_instruction = 'left'
    elif sum>0 and sum%2 == 0:
        last_instruction = 'right'

    print(last_instruction, steps)
    instruction = input()