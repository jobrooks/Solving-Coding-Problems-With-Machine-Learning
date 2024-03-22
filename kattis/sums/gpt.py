# 3.5 wrong answer 0/7
T = int(input())

for _ in range(T):
    N = int(input())
    a, b = 1, 2
    s = a + b
    
    while s < N:
        b += 1
        s += b
        
        while s > N:
            s -= a
            a += 1
        
        if s == N:
            print(f"{N} = {' + '.join(str(i) for i in range(a, b+1))}")
            break
    
    if s != N:
        print("IMPOSSIBLE")
