T = int(input())
mod = 10**9 + 7

def calc_ways(r, c):
    if r == 1 or c == 1:
        return 3
    return (calc_ways(r - 1, c) * 3) % mod

for _ in range(T):
    r, c = map(int, input().split())
    print(calc_ways(r, c))