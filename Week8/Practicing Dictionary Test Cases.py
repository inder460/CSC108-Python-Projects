def inc_count(d: dict[object, int], k: object) -> None:
    '''
    k is immutable. Increment the value associated with k
    in d. If k is not a key in d, add k with value 1.
    >>> d = {'a': 1, 'c': 3}
    >>> inc_count(d, 'a')
    >>> d == {'a': 2, 'c': 3}
    True
    '''
    if k not in d:
        d[k] = 1
    else:
        d[k] = d[k] + 1