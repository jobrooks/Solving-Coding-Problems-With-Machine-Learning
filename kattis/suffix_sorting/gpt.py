# 5.9 runtime error 0/2
def construct_suffix_array(s):
    # Construct the suffix array of s in O(n log n) time
    # using the Manber-Myers algorithm
    n = len(s)
    sa = list(range(n))
    sa.sort(key=lambda i: s[i:])
    return sa

def find_starting_positions(s, n, queries):
    # Construct the suffix array of s
    sa = construct_suffix_array(s)

    # Answer each query
    positions = []
    for q in queries:
        # Binary search for the q-th smallest suffix
        lo, hi = 0, len(s)
        while lo < hi:
            mid = (lo + hi) // 2
            if s[sa[mid]:] < s[q:]:
                lo = mid + 1
            else:
                hi = mid
        positions.append(sa[lo])

    return positions

# Read input
while True:
    try:
        s = input().strip()
        n = int(input())
        queries = list(map(int, input().split()))

        # Find starting positions of each query
        positions = find_starting_positions(s, n, queries)

        # Print output
        print(' '.join(str(p) for p in positions))

    except EOFError:
        break
