import sys

Q, M, S1, S2 = map(int, input().split())
distance = [0] * (M + 1)
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        p, h = map(int, query[1:])
        distance[p] = h
    else:
        p = int(query[1])
        distance[p] = 0

    hits = 0
    curr_distance = 0
    turn = 0
    while curr_distance <= M:
        curr_distance += 1
        if distance[curr_distance] > 0:
            if turn % 2 == 0:
                S1 += distance[curr_distance]
            else:
                S2 += distance[curr_distance]
        if turn % 2 == 0:
            curr_distance += S1
        else:
            curr_distance += S2
        turn += 1

    sys.stdout.write(str(hits) + '\n')
    sys.stdout.flush()