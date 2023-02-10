from typing import TextIO
from io import StringIO


def three_lines(f: TextIO) -> list[list[str]]:
    '''
    f is a movie music rating file.
    Return a list containing 3 elements:
    the movies, the songs, and the song ratings

    >>> input_file = open('songs.txt')
    >>> three_lines(input_file)
    [['Aladdin', 'Frozen', 'The Lion King', 'The Little Mermaid', 'Aladdin'], ['Friend Like Me', 'Let It Go', 'Be Prepared', 'Part Of Your World', 'A Whole New World'], ['9', '4', '11', '10', '6']]

    >>> sample = """Movie Songs and Ratings
    ... # These are Dan's ratings
    ... # Visit Dan in office hours to discuss
    ... # Aladdin, Friend Like Me, 9"""
    >>> three_lists(StringIO(sample))
    [['Aladdin'], ['Friend Like Me'], ['9']]
    '''
    movies = []
    songs = []
    ratings = []

    f.readline()
    line = f.readline()
    while line.startswith('#'):
        line = f.readline()
    while line:
        lst = line.strip().split(', ')
        movies.append(lst[0])
        songs.append(lst[1])
        ratings.append(lst[2])
        line = f.readline()
    return [movies, songs, ratings]
