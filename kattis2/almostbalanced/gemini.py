from collections import defaultdict

n, m = map(int, input().split())

# initialize the map with default value = 0
conditions = defaultdict(int)

for _ in range(m):
    t, l, r, v = map(int, input().split())
    # update the map with specific condition count
    conditions[(l, r)] += (t, v)

# initialize the string with all 1s
string = '1' * n

for (l, r), conditions_list in conditions.items():
    # get the maximum number of 0's allowed in the range
    max_zeros = max(v for t, v in conditions_list if t == 0)
    # get the maximum number of 1's allowed in the range
    max_ones = max(v for t, v in conditions_list if t == 1)

    # replace 1's with 0's if the number of 1's exceeds the allowed limit
    if max_ones < r - l + 1 - max_zeros:
        for i in range(l, r + 1, 2):
            string = string[:i] + '0' + string[i + 1:]

    # replace 0's with 1's if the number of 0's exceeds the allowed limit
    elif max_zeros < r - l + 1 - max_ones:
        for i in range(l, r + 1, 2):
            string = string[:i] + '1' + string[i + 1:]

# print the lexicographically smallest string
print(string)