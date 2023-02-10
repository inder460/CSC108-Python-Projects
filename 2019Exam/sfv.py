def lastname_dict(names: list[list[str]]) -> dict[str, list[str]]:
    """Given a list of [last-name, first-name] entries, return a dictionary mapping
    last-names to the list of first-names with that last-name.
    >>> lastname_dict([["Universe", "Steven"], ["Universe", "Greg"], ["Loot", "Mike"]])
    {'Universe': ['Steven', 'Greg'], 'Loot': ['Mike']}
    """
    ans = {}

    for last_name, first_name in names:
        if last_name in ans:
            ans[last_name] += first_name
        else:
            ans[last_name] = first_name
    return ans