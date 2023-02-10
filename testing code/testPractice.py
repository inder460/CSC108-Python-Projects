x = input()

result = ''
counter = 1
for i in x:
    t = ord('a')
    distance = ord(i) - t + counter
    if distance >= 26:
        distance = distance - 26
    counter += 1
    result = result + chr(t + distance)

print(result)

