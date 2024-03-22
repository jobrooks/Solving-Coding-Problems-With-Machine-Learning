# 1.3 wrong answer 0/99

a = int(input())

# Compute the ratio for option one
ratio_one = (100 - a) / a

# Compute the ratio for option two
ratio_two = a / (100 - a)

print(f"1:{ratio_one:.3f}")
print(f"1:{ratio_two:.3f}")
