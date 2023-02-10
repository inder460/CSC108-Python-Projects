def merge_dict(d1: dict[object, int], d2: dict[object, int]) -> None:
    '''
    Add key/value pairs from d2 into d1. If a key from d2 already
    appears in d1, the new value in d1 is the sum of the values. If a
    key appears only in d1 or d2, then the new value in d1 is the
    original value from the dictionary that contained this key.
    d2 is unchanged.
    >>> d1 = {5: 3, 4: 2}
    >>> d2 = {4: 7, 6: 3}
    >>> merge_dict(d1, d2)
    >>> d1 == {4: 9, 5: 3, 6: 3}
    True
    '''
    for key in d2:
        if key in d1:
            d1[key] = d1[key] + d2[key]
        else:
            d1[key] = d2[key]
