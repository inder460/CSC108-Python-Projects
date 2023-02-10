def binary_search(lst: list[int], x: int) -> int:
    '''
    >>> binary_search([2, 3, 4, 10, 40], 10)
    3
    >>> binary_search([2, 3, 4, 10, 10, 10, 40], 10)
    3
    '''

    low = 0
    high = len(lst) - 1
    mid = 0

    while low <= high:
        mid = (low+high)//2

        if list[mid] > x:
            high = mid - 1
        elif lst[mid] < x:
            low = mid + 1
        else: # found target x
            return mid
    return -1
