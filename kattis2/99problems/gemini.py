n = int(input())
closest = n + (100 - n % 100)

if n <= closest / 2:
    closest -= 100

print(closest)