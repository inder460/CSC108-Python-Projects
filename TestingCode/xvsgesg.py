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
    while line != '':  # Line 4
        line = line.split()  # Line 5
        for i in range(len(line)):  # Line 6
            if line[i] in allergies:  # Line 7
                line[i] = 'REMOVED'  # Line 8
        clean_shopping_lists.write(f'{" ".join(line)}\n')  # Line 9
        line = shopping_lists.readline()  # Line 10


allergy_checker('shopping_lists.txt', 'clean_shopping_list', 'pizza')
