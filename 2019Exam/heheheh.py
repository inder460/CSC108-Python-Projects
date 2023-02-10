def make_dictionary(file_name: str) -> dict[str, int]:
    """Given the name of a grade file file_name, return a dictionary
    that maps student numbers to grades.
    Assuming "grades.txt" contains the four records in the example
    file above
    >>> d = make_dictionary("grades.txt")
    >>> d["101029383"]
    80
    >>> d["292833315"]
    51
    >>> len(d)
    4
    """
    grade_file = open(file_name, "r")
    grades = {}
    grade_file = grade_file.readlines()
    for line in grade_file:
        grades[line[:line.split(',')]] = line[line.split(','):]

    return grades