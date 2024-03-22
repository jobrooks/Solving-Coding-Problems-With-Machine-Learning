# 5.2 Wrong Answer 0/30
from collections import defaultdict

# read input
S = input().strip()
n, q = map(int, input().split())
words = [input().strip() for _ in range(n)]

# preprocess dictionary
char_indices = defaultdict(list)
for i, c in enumerate(S):
    char_indices[c].append(i)

word_indices = []
for word in words:
    indices = []
    for c in word:
        indices.append(char_indices[c])
    word_indices.append(indices)

# process queries
for _ in range(q):
    l, r, k = map(int, input().split())
    l -= 1
    r -= 1
    subseq_indices = word_indices[k-1][0]
    for indices in word_indices[k-1][1:]:
        subseq_indices = [i for i in subseq_indices if i in indices]
    candidates = [words[k-1][i:j+1] for i in subseq_indices for j in subseq_indices if i <= j]
    candidates.sort()
    if k > len(candidates):
        print("NO SUCH WORD")
    else:
        print(candidates[k-1][:10])
