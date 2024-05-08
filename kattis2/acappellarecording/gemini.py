# 3.6 Error 2/17
import sys

def main():
    n, d = map(int, sys.stdin.readline().split())
    notes = [int(sys.stdin.readline()) for _ in range(n)]

    # Sort the notes in ascending order
    notes.sort()

    # Initialize the minimum number of recordings to 1
    min_recordings = 1

    # Iterate over the notes
    for i in range(n - 1):
        # If the difference between the current note and the next note is greater than d, then we need to create a new recording
        if notes[i + 1] - notes[i] > d:
            min_recordings += 1

    # Print the minimum number of recordings
    print(min_recordings)

if __name__ == "__main__":
    main()