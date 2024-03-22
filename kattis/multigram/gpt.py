# 2.8 wrong answer 0/13
from collections import defaultdict

# read the input word
word = input()

# create a dictionary of character frequencies for each substring
freqs = defaultdict(list)
for i in range(len(word)):
    freq = [0] * 26
    for j in range(i, len(word)):
        freq[ord(word[j]) - ord('a')] += 1
        freqs[tuple(freq)].append((i, j))

# check each substring for mutual anagramness
for freq, substrings in freqs.items():
    for i in range(len(substrings)):
        root = word[substrings[i][0]:substrings[i][1]+1]
        for j in range(i+1, len(substrings)):
            anagram = word[substrings[j][0]:substrings[j][1]+1]
            if sorted(root) == sorted(anagram):
                root = min(root, anagram)
        if sorted(root) == sorted(word):
            print(root)
            exit()

# if no multigram is found, output -1
print(-1)
