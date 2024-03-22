# 2.5 accepted 3/3

import sys

def closest_sum(nums, q):
    closest = float('inf')
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            total = nums[i] + nums[j]
            if abs(total - q) < abs(closest - q):
                closest = total
    return closest

case = 1
while True:
    try:
        n = int(input())
    except:
        break
    
    nums = []
    for i in range(n):
        nums.append(int(input()))
        
    nums.sort()
    
    print(f"Case {case}:")
    case += 1
    
    m = int(input())
    for i in range(m):
        q = int(input())
        res = closest_sum(nums, q)
        print(f"Closest sum to {q} is {res}.")
