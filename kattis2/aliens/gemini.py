m = int(input())
while m > 0:
    s = input()
    n = len(s)
    occurrences = []
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            count = s.count(substring)
            if count >= m:
                occurrences.append((len(substring), j))
    if not occurrences:
        print("none")
    else:
        occurrences.sort(key=lambda x: (x[0], -x[1]))
        print(occurrences[0][0], occurrences[0][1])
    m = int(input())