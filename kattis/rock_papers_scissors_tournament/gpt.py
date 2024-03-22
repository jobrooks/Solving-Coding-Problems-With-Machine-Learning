# 4.0 runtime error 0/2

while True:
    n, k = map(int, input().split())
    if n == 0:
        break
    
  
  
  # Initialize the win and loss counters for each player
    wins = {i: 0 for i in range(1, n+1)}
    losses = {i: 0 for i in range(1, n+1)}
    
    # Play k games between each pair of players
    for _ in range(k*n*(n-1)//2):
        p1, m1, p2, m2 = input().split()
        m1 = m1.lower()
        m2 = m2.lower()
        
        # Determine the outcome of the game and update the counters
        if m1 == m2:
            continue
        elif m1 == 'rock' and m2 == 'scissors' or \
             m1 == 'paper' and m2 == 'rock' or \
             m1 == 'scissors' and m2 == 'paper':
            wins[int(p1)] += 1
            losses[int(p2)] += 1
        else:
            wins[int(p2)] += 1
            losses[int(p1)] += 1
    
    # Calculate and output the win averages for each player
    for i in range(1, n+1):
        total = wins[i] + losses[i]
        if total == 0:
            print('-')
        else:
            print('{:.3f}'.format(wins[i]/total))
    
    # Output a blank line between cases
    print()
