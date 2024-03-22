# 3.1 wrong answer 1/6
n, m = map(int, input().split())

# read the notes playable by each instrument
instruments = []
for i in range(n):
    notes = set(map(int, input().split()[1:]))
    instruments.append(notes)

# read the notes of the tune
tune = list(map(int, input().split()))

# play the tune
current_instrument = 0
switches = 0
for note in tune:
    if note not in instruments[current_instrument]:
        # find the next instrument that can play this note
        for i in range(n):
            if note in instruments[i]:
                current_instrument = i
                switches += 1
                break
    # play the note with the current instrument
    # and move to the next note
    else:
        continue

print(switches)
