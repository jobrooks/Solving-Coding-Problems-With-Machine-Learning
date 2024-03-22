# 3.5 wrong answer 2/13

k, m, n = map(int, input().split())

if (k // (m + n)) % 2 == 0:
    # If the total number of rounds is even, Alex wins
    if k % (m + n) == 0 or k % (m + n) >= m:
        print("Alex")
    else:
        print("Barb")
else:
    # If the total number of rounds is odd, Barb wins
    if k % (m + n) == 0 or k % (m + n) <= n:
        print("Barb")
    else:
        print("Alex")
