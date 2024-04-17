import sys
input = sys.stdin.readline

def game(k, m, n):
    if k % (n + 1) <= m:
        return "Alex"
    else:
        return "Barb"

k, m, n = map(int, input().split())
print(game(k, m, n))