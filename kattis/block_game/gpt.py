# 3.5 wrong answer 2/20

n, m = map(int, input().split())

# If the smaller stack evenly divides the larger stack,
# the second player will be forced to empty it and the
# first player will win
if min(n, m) == 1 or max(n, m) % min(n, m) == 0:
    print("win")
else:
    print("lose")
