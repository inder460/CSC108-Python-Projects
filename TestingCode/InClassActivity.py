text = input()

result = ''

for char in text:
    base = ord('a')
    distance = ord(char) - base + 3
    if distance >= 26:
        distance = distance - 26
    result = result + chr(base + distance)

print(result)