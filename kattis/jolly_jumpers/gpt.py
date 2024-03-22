# 3.5 accepted 3/3
import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))[1:]
    diffs = [abs(nums[i] - nums[i-1]) for i in range(1, len(nums))]
    expected_diffs = set(range(1, len(nums)))
    if set(diffs) == expected_diffs:
        print("Jolly")
    else:
        print("Not jolly")
