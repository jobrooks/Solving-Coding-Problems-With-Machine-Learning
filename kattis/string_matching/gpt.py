# 4.4 accepted 2/2
import sys

def compute_failure_function(pattern):
    m = len(pattern)
    failure = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j-1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j
    return failure

def find_occurrences(pattern, text):
    n, m = len(text), len(pattern)
    failure = compute_failure_function(pattern)
    j = 0
    occurrences = []
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j-1]
        if text[i] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i-m+1)
            j = failure[j-1]
    return occurrences

for line in sys.stdin:
    pattern = line.strip()
    text = input().strip()
    occurrences = find_occurrences(pattern, text)
    print(" ".join(str(i) for i in occurrences))
