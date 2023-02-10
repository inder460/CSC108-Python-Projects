from io import StringIO

import bard
from bard import read_input

def make_file(villagers: list[str], songs: list[str], parties: list[str]) -> TextIO:
    v_str = "\n".join(villagers) + ("\n" if villagers else "")
    s_str = "\n".join(songs) + ("\n" if songs else "")
    p_str = "\n".join(parties) + ("\n" if parties else "")
    s = f"VILLAGERS\n{v_str}\nSONGS\n{s_str}\nPARTIES\n{p_str}"
    return StringIO(s)

villagers = {"Damien Rice", "Drake*"}
songs = {"Rule, Britannia"}
parties = ["Damien Rice,Drake", "Damien Rice"]
v, b, s, p = bard.read_input(make_file(villagers, songs, parties))


def sing_at_party(
        villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]
) -> None:
    """
    A bard sings if present, otherwise the villagers sing.
    """
    for person in party:
        for bard in bards:
            if person == bard:
                for villager in villagers:
                    if villager != bard:
                        villagers[villager] += songs[bard]
            else:
                break

