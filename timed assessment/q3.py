"""
Q3: Writing a Function
3 marks

Write the code for the following function.
"""

def unmask_chars(s1: str, s2: str, mask: str) -> str:
    '''
    Return a new string where the character at index i is
    s1[i] if mask[i] is 0
    and s2[i] if mask[i] is 1.

    len(s1), len(s2), and len(mask) are equal.

    >>> unmask_chars('cat', 'bat', '001')
    'cat'
    >>> unmask_chars('a', 'b', '0')
    'a'
    >>> unmask_chars('apple', 'graph', '01011')
    'arpph'
    '''

    # TODO: Write your code here
    ans = ""
    for i in range(len(mask)):
        if mask[i] == '0':
            ans += s1[i]
        else:
            ans += s2[i]
    return ans
