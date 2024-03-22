# 3.8 wrong answer 1/7

c = float(input())

# The maximum hardness is achieved when x = y = c/2 and z = 1 - c
# We can compute this value directly as xy = (c/2) * (c/2) = c^2 / 4
# and x + y = c, so the hardness is xy = (c/2) * (c/2) = c^2 / 4

print("{:.6f}".format(c*c/4))
