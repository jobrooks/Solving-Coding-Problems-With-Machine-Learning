# 4.6 accepted 17/17
def can_cut_trees(heights, H, M):
    wood = 0
    for height in heights:
        if height > H:
            wood += height - H
    return wood >= M

N, M = map(int, input().split())
heights = list(map(int, input().split()))

lo, hi = 0, max(heights)
while lo < hi:
    mid = (lo + hi + 1) // 2
    if can_cut_trees(heights, mid, M):
        lo = mid
    else:
        hi = mid - 1

print(lo)
