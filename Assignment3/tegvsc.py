
villagers = {"Drake", "Damien Rice*"}
songs = {"Call Me Maybe", "Lonely", "Square Enix Medley"}
parties = ["Damien Rice,Drake", "Drake"]


vill_songs = set()
for key, val in villagers.items():
    for i in val:
        vill_songs.add(i)
all_songs = set()
for key, val in songs.items():
    for i in val:
        all_songs.add(i)
all_songs.difference(vill_songs)
print(all_songs)