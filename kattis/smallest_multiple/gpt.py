# 3.4 accepted 2/2
import math

def lcm(a, b):
    return (a*b) // math.gcd(a, b)

def lcm_set(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = lcm(result, nums[i])
    return result

while True:
    try:
        nums = list(map(int, input().split()))
        print(lcm_set(nums))
    except EOFError:
        break
