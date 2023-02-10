string = input()

new_string = ''
for i in range(len(string)):
    if string[i] != ' ':
        new_string = new_string + string[i]
print(new_string)


