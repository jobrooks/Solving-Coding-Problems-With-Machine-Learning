# 3.3 accepted 2/2

import sys
from math import factorial

def count_anagrams(word):
    freq = {}
    for letter in word:
        freq[letter] = freq.get(letter, 0) + 1
    num_anagrams = factorial(len(word))
    for count in freq.values():
        num_anagrams //= factorial(count)
    return num_anagrams

for line in sys.stdin:
    word = line.strip()
    print(count_anagrams(word))
