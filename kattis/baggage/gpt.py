# 5.2 wrong answer 0/40

n = int(input())

# Initialize list of positions for the bins
bins = list(range(-2*n+1, 2*n, 2))

# Calculate the position of the last A bin
last_a = -2*n + 2*(n//2)

# Initialize list of moves
moves = []

# Iterate over the B bins and move them to the right of the A bins
for i in range(1, 2*n-1, 2):
    if bins[i] > last_a:
        # Move the bin to the left of the last A bin
        moves.append((i, last_a+1))
        # Update the position of the last A bin
        last_a += 2

# Print the list of moves
for move in moves:
    print(move[0], "to", move[1])
