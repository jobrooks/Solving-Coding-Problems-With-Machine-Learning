# 2.7 wrong answer 0/47

n, m = map(int, input().split())

# create a list of tuples representing the researchers
researchers = []
for i in range(n):
    a, s = map(int, input().split())
    researchers.append((a, a + s))

# sort the researchers by their arrival time
researchers.sort()

# initialize a list to keep track of the end time of each workstation
workstations = [0] * n

# initialize a variable to keep track of the number of unlockings saved
unlockings_saved = 0

for i in range(n):
    assigned = False
    for j in range(n):
        # check if the workstation is available
        if researchers[i][0] >= workstations[j]:
            # assign the researcher to the workstation
            workstations[j] = researchers[i][1] + m
            assigned = True
            break
    if not assigned:
        # if no workstation is available, increment the number of unlockings saved
        unlockings_saved += 1

print(unlockings_saved)
