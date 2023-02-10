def word_pattern(pattern: str, words: list[str]) -> bool:
    '''Given a pattern and a word list, determine if the word list follows
    the same pattern. That is to say, ensure that
    pattern[j] == pattern[k] only when words[j] == words[k]
    and
    pattern[j] != pattern[k] means words[j] != words[k]
    Precondition: Assume pattern is all lowercase letters.
    >>> word_pattern('aaaa', ['cat', 'cat', 'cat', 'cat'])
    True
    >>> word_pattern('yoox', ['dog', 'cat', 'cat', 'fish'])
    True
    >>> word_pattern('xy', ['cat', 'cat'])
    False
    >>> word_pattern('xoox', ['dog', 'cat', 'cat', 'fish'])
    False
    '''
    x = len(pattern)
    p1 = pattern[:(x/2)]
    p2 = pattern[(x/2):]
    y = len(words)
    w1 = []
    w1 = y[:(y/2)]
    w2 = []
    w2 = y[(y/2):]

    for i in len(w1):
        for j in len(w2):
            if p1[i] == p2[j] and w1[i] == w1[j]:
                return True
            else:
                return False