from collections import defaultdict
MAX_LENGTH = 40000
m = 1
while m != 0:
    m = int(input())
    if m == 0:
        break
    s = input()
    length = len(s)
    count = defaultdict(lambda: [0] * length)
    for i in range(length):
        for j in range(length):
            if i == j:
                count[s[i]][i] = 1
            elif s[i] == s[j] and count[s[i]][j - 1] > 0:
                count[s[i]][j] = count[s[i]][j - 1] + 1
    max_length = 0
    max_r = -1
    for i in count:
        for j in range(length - m + 1):
            if count[i][j + m - 1] - (count[i][j - 1] if j > 0 else 0) >= m:
                current_length = j + m - count[i][j + m - 1]
                if current_length > max_length or (current_length == max_length and j > max_r):
                    max_length = current_length
                    max_r = j
    if max_length == 0:
        print("none")
    else:
        print(max_length, max_r)