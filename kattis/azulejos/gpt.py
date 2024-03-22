# 5.1 wrong answer 0/33
n = int(input())
back_price = list(map(int, input().split()))
back_height = list(map(int, input().split()))
front_price = list(map(int, input().split()))
front_height = list(map(int, input().split()))

# Sort both rows by price in non-decreasing order
back_indices = sorted(range(n), key=lambda i: back_price[i])
front_indices = sorted(range(n), key=lambda i: front_price[i])

# Create initial ordering of tiles
back = [back_indices[i] + 1 for i in range(n)]
front = [front_indices[i] + 1 for i in range(n)]

# Iterate over tiles in back row
for i in range(n):
    tile_i = back[i]
    j = n - 1
    while j >= 0:
        tile_j = front[j]
        if front_height[tile_j - 1] < back_height[tile_i - 1]:
            front.pop(j)
            front.insert(j+1, tile_i)
            break
        j -= 1
    else:
        print("impossible")
        exit()

# Output ordering of tiles
print(" ".join(str(x) for x in back))
print(" ".join(str(x) for x in front))
