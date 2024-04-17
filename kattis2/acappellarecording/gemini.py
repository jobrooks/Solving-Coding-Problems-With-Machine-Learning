import sys

def main():
    n, d = map(int, sys.stdin.readline().split())
    notes = [int(sys.stdin.readline()) for _ in range(n)]

    notes.sort()

    min_recordings = 1
    current_min = notes[0]
    current_max = notes[0]

    for i in range(1, n):
        if notes[i] - current_min > d or current_max - notes[i] > d:
            min_recordings += 1
            current_min = notes[i]
            current_max = notes[i]
        else:
            current_min = min(current_min, notes[i])
            current_max = max(current_max, notes[i])

    print(min_recordings)

if __name__ == "__main__":
    main()