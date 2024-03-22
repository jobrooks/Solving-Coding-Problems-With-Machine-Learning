# 5.7 wrong answer 0/56
def merge_ranges(cams):
    cams.sort()  # sort by start of range
    merged = []
    for cam in cams:
        if merged and cam[0] <= merged[-1][1]:  # overlap
            merged[-1] = (merged[-1][0], max(merged[-1][1], cam[1]))  # extend previous range
        else:
            merged.append(cam)
    return merged


n, k = map(int, input().split())
walls = [0] * n  # array to keep track of which walls have been covered
cams = []
for i in range(k):
    a, b = map(int, input().split())
    if a <= b:
        cams.append((a-1, b-1))
        walls[a-1:b] = [1] * (b - a + 1)  # mark walls as covered
    else:
        cams.append((a-1, n-1))
        cams.append((0, b-1))
        walls[a-1:] = [1] * (n - a + 1)  # mark walls as covered
        walls[:b] = [1] * b  # mark walls as covered
merged = merge_ranges(cams)
if merged[0][0] == 0 and merged[-1][1] == n-1:  # check if whole building is covered
    print(len(merged))
else:
    print("impossible")
