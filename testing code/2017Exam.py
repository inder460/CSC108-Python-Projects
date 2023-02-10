from typing import TextIO


def read(input_file: TextIO) -> list[list[int]]:

    lst1 = []
    x = input_file.readlines()
    for i in x:
        i = i.split()
        if '\n' in i:
            i.remove('\n')
        lst1.append(i)
    return lst1


reader = open('hdbhb', 'r')
print(read(reader))

