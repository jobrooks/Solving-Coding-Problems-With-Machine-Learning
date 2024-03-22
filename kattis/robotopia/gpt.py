# 5.4 wrong answer 0/20
n = int(input())

for _ in range(n):
    l1, a1, l2, a2, lt, at = map(int, input().split())

    found = False
    for i in range(1, lt):
        if (lt - i * l1) % l2 == 0:
            j = (lt - i * l1) // l2
            if i * a1 + j * a2 == at:
                print(i, j)
                found = True
                break
    
    if not found:
        print("?")
