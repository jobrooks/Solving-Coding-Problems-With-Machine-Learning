# 2.2 wrong answer 0/24

n, m = map(int, input().split())

slimes = 0
while m > 0:
    # Check if the number of slimes is odd, which means the baby panda sneezed
    if m % 2 == 1:
        slimes += 1
    
    # Divide the number of slimes by 2 to simulate the overnight splitting
    m //= 2
    n -= 1

# If there are any days left, the baby panda didn't sneeze on those days
if n > 0:
    slimes = 0

print(slimes)