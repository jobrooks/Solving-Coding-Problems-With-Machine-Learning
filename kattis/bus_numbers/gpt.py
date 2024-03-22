# 2.5 accepted 20/20

n = int(input())  # number of buses
buses = sorted(map(int, input().split()))  # list of bus numbers, sorted

i = 0
output = []
while i < n:
    j = i
    while j < n - 1 and buses[j + 1] == buses[j] + 1:
        j += 1
    if j == i:
        output.append(str(buses[i]))
    elif j == i + 1:
        output.extend([str(buses[i]), str(buses[j])])
    else:
        output.append(str(buses[i]) + '-' + str(buses[j]))
    i = j + 1

print(' '.join(output))
