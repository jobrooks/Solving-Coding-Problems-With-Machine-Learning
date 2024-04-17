import bisect

def main():
    n, k = map(int, input().split())
    times = []
    for _ in range(n):
        a, b = map(int, input().split())
        times.append((a, 1))
        times.append((b, -1))
    times.sort()

    max_friends = 0
    cur_friends = 0
    cur_time = 0
    for time, delta in times:
        if cur_time + delta <= k:
            cur_friends += delta
            max_friends = max(max_friends, cur_friends)
        cur_time = time

    print(max_friends)

if __name__ == "__main__":
    main()