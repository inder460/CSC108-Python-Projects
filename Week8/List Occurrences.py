def count_occurrences(L: list) -> dict[object, int]:
    """
    Return a dictionary in which the keys are the items in L,
    and their associated values are integers denoting the number
    of times the item is contained in L.

    >>> count_occurrences([8, 9, 8, 8, 9, 'inder', 'inder'])
    {8: 3, 9: 2, 'inder': 2}
    """

    d = {}
    for item in L:
        d[item] = d.get(item, 0) + 1
    return d