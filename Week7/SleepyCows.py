input_file = open('herding.in', 'r')
output_file = open('herding.out', 'w')

lst = input_file.readline().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
lst.sort()

if lst[1] - lst[0] == 1 and lst[2] - lst[1] == 1:
    min_moves = 0
elif lst[1] - lst[0] == 2 or lst[2] - lst[1] == 2:
    min_moves = 1
else:
    min_moves = 2
output_file.write(f'{min_moves}\n')

gap1 = lst[1] - lst[0] - 1
gap2 = lst[2] - lst[1] - 1

if gap1 > gap2:
    max_moves = gap1
else:
    max_moves = gap2

output_file.write(f'{max_moves}')

input_file.close()
output_file.close()