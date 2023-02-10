bmd_type = dict[str, dict[int, list[str]]]

def most_covered(bmd:bmd_type) -> str:
    """
    bmd is a birthday month dictionary with at least one key. Return
    the name of the month that is most "covered" in the dictionary.
    I.e., the month with the most days on which someone has a birthday. If
    there is a tie, return any month with that maximum coverage.

    >>> bmd = {'February': {13: ['Catherine']}, 'May': {3: ['Katie'], 8: ['Peter', 'Ed']}}
    >>> most_covered(bmd)
    'May'
    """
    most = 0

    for month in bmd:
        if len(bmd[month])>most:
            most = len(bmd[month])
            best_month = month
    return best_month