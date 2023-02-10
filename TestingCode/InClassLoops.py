String = input()
count = 0

for char in String:
    if char == 'a' or char == 'A':
        count = count + 1
    elif char == 'e' or char == 'E':
        count = count + 1
    elif char == 'i' or char == 'I':
        count = count + 1
    elif char == 'o' or char == 'O':
        count = count + 1
    elif char == 'u' or char == 'U':
        count = count + 1
print(count)