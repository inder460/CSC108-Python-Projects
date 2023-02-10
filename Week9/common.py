def common_chars(s1: str, s2: str) -> tuple[int, int]:
    '''
    Return a tuple where the first element is the number of positions where s1
    and s2 have the same chars, and the second element is the number of positions
    where s1 and s2 have the same char ignoring case.

    >>> common_chars('acde', 'axe')
    (1, 1)
    >>> common_chars('xaxc', 'bAac')
    (1, 2)
    >>> common_chars('ABC', 'abc')
    (0, 3)
    >>> common_chars('', '')
    (0, 0)
    '''
    shorter_len = min(len(s1), len(s2))
    exact = 0
    insensitive = 0
    for i in range(shorter_len):
        if s1[i] == s2[i]:
            exact += 1
        if s1[i].lower() == s2[i].lower():
            insensitive += 1
    return exact, insensitive
