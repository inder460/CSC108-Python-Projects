"""
A BARD DAY'S NIGHT
a.k.a. BARD ROCK CAFE
a.k.a. THE SCHOOL OF BARD KNOCKS
a.k.a. A BARD RAIN'S A-GONNA FALL
"""

# Imports

from typing import Optional, TextIO  # Specific annotations

from math import ceil  # For stats

# Constants

# Minimum number of songs for a villager to be promoted to a bard
BARD_THRESHOLD = 10

# Number of songs for the billboard_top statistic
BILLBOARD_N = 10


# DO NOT use these as variables in your code;
# they are only for type contracts.

# Maps from {name: songs that this villager knows}
villagers_type = dict[str, set[str]]

bards_type = set[str]

# Maps from {song name: names of people, including bards, that know this song}
songs_type = dict[str, set[str]]

# A list of parties; each party is a set of the attendee names
parties_type = list[set[str]]

def read_input(f: TextIO,) -> tuple[villagers_type, bards_type, songs_type, parties_type]:
    """
    Read the given file and return the villagers, bards, songs, and parties.

    f is an open file containing VILLAGERS and bards, SONGS, and PARTIES,
    in that order. One villager or bard per line;
    one song per line; one party per line, consisting of attendees
    separated by commas. The parties are given in the order they're held.
    """
    line = f.readline()
    villagers_type = {}
    bards_type = set()
    songs_type = {}
    parties_type = []
    line = f.readline().rstrip()
    while line.rstrip() != "":
        if line[-1] == "*":
            bards_type.add(line[0:-1])
        else:
            villagers_type.update({line: set()})
        line = f.readline().rstrip()
    line = f.readline()
    line = f.readline().rstrip()
    songsList = []
    while line.rstrip() != "":
        songsList.append(line)
        line = f.readline().rstrip()
    songsList.sort()
    for i in range(len(songsList)):
        songs_type.update({songsList[i]: bards_type.copy()})      
    line = f.readline()
    line = f.readline().rstrip()
    while line.rstrip() != "":
        listSet = line.split(",")
        parties_type.append(set(listSet))
        line = f.readline().rstrip()
    return (villagers_type, bards_type, songs_type, parties_type)

# Party functions
# We highly recommend adding helper functions here!   
def intersect(set1: set, set2: set) -> bool:
    if set1.intersection(set2):
        return True
    else:
        return False

def bardCounter(bards: bards_type, party: set[str]) -> int:
    bardCount = 0
    for i in party:
        if i in bards:
            bardCount = 1
    return bardCount

def bard_sings(villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]):
    lastSong = ""
    lastParty = set()
    songItem = list(songs.items())
    for name in party:
        count = 0
        if name in villagers:
            for songName in songs:
                if (name not in songItem[count][1]) and (intersect(lastParty, songItem[count][1]) == False):
                    lastSong = str(songName)
                    lastParty.add(name)
                    break
                count = count + 1   
    if lastSong != "":            
        for i in party:
            if i in villagers:
                villagers[i].add(lastSong)
                songs[lastSong].add(i)
    
def villager_sings(villagers: villagers_type, songs: songs_type, party: set[str]): 
    for k in party:
        knownSongs = villagers[k]
        for i in party:
            villagers[i].update(knownSongs)
            if villagers[i]:
                for j in villagers[i]:
                    songs[j].add(i)

def sing_at_party(villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]) -> None:
    """
    A bard sings if present, otherwise the villagers sing.
    """
    bardCount = bardCounter(bards, party)
    if bardCount == 1:
        bard_sings(villagers, bards, songs, party)        
    else:
        villager_sings(villagers, songs, party)

def update_bards_after_party(villagers: villagers_type, bards: bards_type, songs: songs_type, party: set[str]) -> None:
    """
    Promote attendees who have learned enough songs to bards,
    iff there is another bard present at the party.
    """
    bardCount = bardCounter(bards, party)
    if bardCount == 1:
        for i in party:
            if i in villagers:
                if len(villagers[i]) >= BARD_THRESHOLD:
                    bards.add(i)
                    villagers.pop(i)
                    for j in songs:
                        songs[j].add(i)

# Stats functions

def unheard_songs(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> set[str]:
    """
    Return a set of songs that have never been heard by non-bards.
    (This means that only the bards know it.)
    """
    unknownSet = set()
    for i in songs:
        if len(songs[i]) == len(bards):
            unknownSet.add(i)
    return unknownSet

def invert_dictionary(d):
    """
    d is a dictionary mapping strings to numbers.
    Return the inverted dictionary of d.
    """
    inverted = {}
    for key in d:
        num = d[key]
        if num not in inverted:
            inverted.update({num: {key}})
        else:
            inverted[num].update({key})
    return inverted

def billboard_top(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> list[str]:
    """
    Return a list of the BILLBOARD_N most popular songs by number of people
    who know them, in descending order. Break ties alphabetically.
    """
    pairs = list(songs.items())
    tempDict = {}
    tempList = []
    billboardList = []
    for i in range(len(pairs)):
        tempDict[pairs[i][0]] = len(pairs[i][1])
        tempList.append(len(pairs[i][1]))
    tempDict = invert_dictionary(tempDict)
    for i in range(BILLBOARD_N - 1):
        alphaList = []
        if tempList:
            maxi = max(tempList)
            for j in tempDict[maxi]:
                alphaList.append(j)
                i = i + 1
                tempList.remove(maxi)
            alphaList.sort()
            billboardList.extend(alphaList)
            tempDict.pop(maxi)
    billboardList = billboardList[:10]
    return billboardList

def all_bards(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> set[str]:
    """Return the set of the village's bards."""
    return bards

def average_attendees(
    villagers: villagers_type,
    bards: bards_type,
    songs: songs_type,
    parties: parties_type,
) -> int:
    """
    Return the average number of attendees at parties in the village.
    Round up to the nearest integer.
    """
    numList = []
    for i in parties:
        numList.append(len(i))
    avg = ceil(sum(numList) / len(numList))
    return avg

# Main process

def run(filename: str) -> dict[str, object]:
    """
    Run the program: read the input, host the parties,
    and return a dictionary of resulting statistics keyed by name:
    unheard_songs, billboard_top, all_bards, average_attendees

    filename is the name of an input file.
    """
    finalDict = {}
    input_file = open(filename, 'r')
    v, b, s, p = read_input(input_file)
    for party in p:
        sing_at_party(v, b , s, party)
        update_bards_after_party(v, b, s, party)
    finalDict['unheard_songs'] = unheard_songs(v, b, s, p)
    finalDict['billboard_top'] = billboard_top(v, b, s, p)
    finalDict['all_bards'] = all_bards(v, b, s, p)
    finalDict['average_attendees'] = average_attendees(v, b, s, p)
    input_file.close()
    return finalDict

# Run program

if __name__ == "__main__":
    # Sample input from the handout -- you can tweak this if you like
    #stats_handout = run("handout_example.txt")
    #print("Results of handout sample input")
    #for key, value in stats_handout.items():
    #    print(f"{key}: {value}")

    #print()
    
    # Sample bigger input -- you can tweak this if you like
    stats_bigger = run("bigger_example.txt")
    print("Results of bigger sample input")
    for key, value in stats_bigger.items():
        print(f"{key}: {value}")