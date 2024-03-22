# 2.6 wrong answer 0/13

n = int(input())  # number of villagers
e = int(input())  # number of evenings

# initialize a set with all villagers
all_villagers = set(range(1, n+1))

# initialize a set with the songs sung on the first evening
songs = set(map(int, input().split()[1:]))

# iterate over the remaining evenings
for _ in range(e-1):
    # read the list of villagers present
    k, *villagers = map(int, input().split()[1:])
    # if the bard is not present, exchange songs
    if 1 not in villagers:
        songs = songs.union(villagers)
    # otherwise, sing a new song
    else:
        new_song = set(villagers[1:])
        # if the new song is different from previous songs, reset the set
        if new_song != songs:
            songs = new_song.copy()

# find the villagers who know all songs
know_all = sorted(villager for villager in all_villagers if songs.issubset({villager}))

# output the result
for villager in know_all:
    print(villager)
