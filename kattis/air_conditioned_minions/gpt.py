# 3.3 wrong answer 8/34

n = int(input())
minions = []
for i in range(n):
    l, u = map(int, input().split())
    minions.append((l, u))

minions.sort()

rooms = []
for minion in minions:
    assigned = False
    for room in rooms:
        if minion[0] <= room[-1][1]:
            room.append(minion)
            assigned = True
            break
    if not assigned:
        rooms.append([minion])

print(len(rooms))
