# 2.4 accepted 2/2

n = int(input())

for i in range(n):
    s, d = map(int, input().split())
    
    # Calculate the two possible scores
    a = (s + d) // 2  # sum of two scores
    b = a - d         # absolute difference between two scores
    
    # Check if the scores are valid
    if a >= 0 and b >= 0 and a + b == s and abs(a - b) == d:
        print(a, b)
    else:
        print("impossible")
