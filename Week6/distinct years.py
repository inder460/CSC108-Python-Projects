def distinct(year: int) -> bool:
    '''
    Return true is digits of year are distinct
    >>> distinct((1234)
    True
    >>> distinct(2022)
    False
    '''
    syear = str(year)
    digits_used = []

    for i in range(len(syear)):
        if syear[i] in digits_used:
            return False
        digits_used.append(syear[i])
    return True


year = int(input())

year = year + 1
while not distinct(year):
    year = year + 1
print(year)
