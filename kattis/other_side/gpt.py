# 5.0 wrong answer 0/42
W, S, C, K = map(int, input().split())

# Function to check if a given state is valid
def is_valid(state):
    if state[1] > state[0] > 0 or state[3] > state[2] > 0:
        return False
    if state[0] + state[1] <= K and state[2] + state[3] <= K:
        return True
    return False

# Start with all items on the left bank
left_bank = [W, S, C, 0]
right_bank = [0, 0, 0, 0]

# Breadth-first search to find a valid sequence of moves
queue = [(left_bank, right_bank)]
visited = set([(tuple(left_bank), tuple(right_bank))])

while queue:
    curr_state = queue.pop(0)
    if curr_state[1][0] == W and curr_state[1][1] == S and curr_state[1][2] == C:
        print("Yes")
        break
    for i in range(4):
        for j in range(4):
            if i != j:
                # Try moving 1 item from i to j
                new_left_bank = curr_state[0].copy()
                new_right_bank = curr_state[1].copy()
                if new_left_bank[i] > 0 and is_valid(new_left_bank):
                    new_left_bank[i] -= 1
                    new_right_bank[j] += 1
                    if (tuple(new_left_bank), tuple(new_right_bank)) not in visited:
                        queue.append((new_left_bank, new_right_bank))
                        visited.add((tuple(new_left_bank), tuple(new_right_bank)))
    else:
        continue
    break
else:
    print("No")
