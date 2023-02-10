"""
Q2: Debugging
3 marks

Consider the following function and attempted body.
"""

from typing import TextIO

def allergy_checker(shopping_lists: TextIO,
                    clean_shopping_lists: TextIO, allergies: list[str]) -> None:
    '''
    shopping_lists is a file open for reading that has at least one food name on every
    non-blank line. Food names are separated by a space.
    Each line in shopping_lists ends with a newline character.
    clean_shopping_lists is a file open for writing.
    allergies is a list of one-word food names.

    Copy lines from shopping_lists to clean_shopping_lists.
    For each food name that is in the allergies list, replace it with 'REMOVED'.
    If a blank line in shopping_lists is reached, stop reading the file.
    '''
    shopping_lists = open(shopping_lists)  # Line 1
    clean_shopping_lists = open(clean_shopping_lists, 'w')  # Line 2
    line = shopping_lists.readline()  # Line 3
    while line.strip():  # Line 4
        line = shopping_lists.readline()  # Line 5
        for i in range(line):  # Line 6
            if line[i] in allergies:  # Line 7
                line[i] = 'REMOVED'  # Line 8
        clean_shopping_lists.write(f'{" ".join(line)}')  # Line 9
        line = shopping_lists.readline()  # Line 10

"""
There may be some bugs or errors in this code that prevent it from working properly.

For each line, indicate:
*OK* if the line is correct
*REMOVE* if the line has to be removed
*CHANGE* if the line has to be changed
 *you must also indicate what the line has to be changed to*


# TODO: tell us what to do with each line

Line 1
ok
Line 2
ok
Line 3
ok
Line 4
change
while line != '':
Line 5
change
line = line.split()
Line 6
change
for i in range(len(line)):
Line 7
ok
Line 8
ok
Line 9
change
clean_shopping_lists.write(f'{" ".join(line)}\n')
Line 10
ok
"""
