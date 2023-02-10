reader = open('testing', 'r')
x = reader.readlines()
for i in x:
    if ('#') in i:
        print(i)