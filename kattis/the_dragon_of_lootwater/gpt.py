# 2.8 accepted 7/7
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    dragon_heads = sorted([int(input()) for _ in range(n)])
    knight_heights = sorted([int(input()) for _ in range(m)])
    
    cost = 0
    i = 0
    
    for head in dragon_heads:
        while i < m and knight_heights[i] < head:
            i += 1
        if i == m:
            print("Loowater is doomed!")
            break
        cost += knight_heights[i]
        i += 1
    
    else:
        print(cost)
