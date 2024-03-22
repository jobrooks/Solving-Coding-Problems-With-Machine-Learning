# 1.6 wrong answer 0/2

n, k = map(int, input().split())

max_passengers = 0
passengers = 0

for i in range(n):
    a, b = map(int, input().split())
    passengers -= a  # subtract passengers who left
    passengers += b  # add passengers who entered
    max_passengers = max(max_passengers, passengers)

# calculate the number of buses needed
buses = (max_passengers + k - 1) // k

print(buses)
