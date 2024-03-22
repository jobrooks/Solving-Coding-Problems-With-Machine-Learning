# 4.1 time limit exception 2/57
s = input()  # read the input string

n = len(s)  # length of the input string

# loop through each k-inversion
for k in range(1, n):
    count = 0  # initialize counter for this k-inversion
    for i in range(n - k):
        j = i + k
        if s[i] == 'B' and s[j] == 'A':
            count += 1
    print(count)
