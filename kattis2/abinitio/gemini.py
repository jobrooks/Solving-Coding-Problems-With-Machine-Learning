from collections import defaultdict

def power(x, y):
    ret = 1
    while y > 0:
        if y % 2 == 0:
            x = x * x
            x = x % mod
            y = y / 2
        else:
            ret = ret * x
            ret = ret % mod
            y = y - 1
    return ret

def hash_function(arr):
    arr.sort()
    ret = 0
    for i in range(len(arr)):
        ret += (arr[i] * power(base, i))
        ret = ret % mod
    return ret

v, e, q = map(int, input().split())
adj = defaultdict(list)

for i in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)

for i in range(q):
    query = int(input())
    if query == 1:
        v += 1
        adj[v] = []
    elif query == 2:
        a, b = map(int, input().split())
        adj[a].append(b)
    elif query == 3:
        a = int(input())
        del adj[a]
    elif query == 4:
        a, b = map(int, input().split())
        adj[a].remove(b)
    elif query == 5:
        new_adj = defaultdict(list)
        for i in adj:
            for j in adj[i]:
                new_adj[j].append(i)
        adj = new_adj
    elif query == 6:
        new_adj = defaultdict(list)
        for i in range(v):
            for j in adj[i]:
                if i not in adj[j]:
                    new_adj[i].append(j)
        adj = new_adj

print(v)
for i in range(v):
    print(len(adj[i]), hash_function(adj[i]))