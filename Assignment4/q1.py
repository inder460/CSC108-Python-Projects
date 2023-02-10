a = input().split()
a_counter = 0
for i in range(len(a)):
    a[i] = int(a[i])
    a_counter += 1

min_diff = 50000000000000000
counter = 0

if len(set(a)) == 1:
    min_diff = 0
else:
    for difficulty in range(len(a)-1):
        difference = abs(a[difficulty] - a[difficulty+1])
        if difference == 0:
            difference = abs(a[counter] - a[counter+1])
            if difference != 0:
                difference = min_diff
        elif difference < min_diff:
            min_diff = difference
        counter += 1
print(min_diff)

