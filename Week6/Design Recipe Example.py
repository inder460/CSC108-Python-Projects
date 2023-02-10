def contest_eligible(cgpa: float, year: int, full_time: bool) -> bool:
    '''
    Given a CGPA, year and whether they are full-time,
    return true iff the student is eligible for te contest.
    >>> contest(3.0, 3, True)
    True
    >>> contest(2.5, 2, False)
    False
    '''
    return (cgpa >= 2) and (year == 2 or year == 3) and full_time