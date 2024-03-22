# 1.4 accepted 10/10

# Read the input from the user
pieces = input().split()

# Define the correct numbers of pieces
correct_pieces = [1, 1, 2, 2, 2, 8]

# Calculate the difference between the correct numbers and the ones found
difference = [correct - int(piece) for correct, piece in zip(correct_pieces, pieces)]

# Output the result
print(*difference)