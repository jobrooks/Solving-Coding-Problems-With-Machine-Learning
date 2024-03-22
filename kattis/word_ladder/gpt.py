# 5.4 wrong answer 0/22

n = int(input())

# Start with a word of length n with all characters the same
start = "a" * n

# Create a list of n words where each word differs from the previous word by exactly one character
words = [start]
for i in range(1, n-1):
    prev_word = words[-1]
    new_word = prev_word[:i] + "a" + prev_word[i+1:]
    while new_word in words:
        j = i
        while j >= 0 and new_word[j] == "z":
            j -= 1
        if j < 0:
            prev_word = words[-2]
            i -= 1
            new_word = prev_word[:i] + "a" + prev_word[i+1:]
            continue
        new_word = new_word[:j] + chr(ord(new_word[j])+1) + new_word[j+1:]
    words.append(new_word)

# The last word in the list will be a word of length n with all characters the same
end = "z" * n
words.append(end)

# Output the word ladder
for word in words:
    print(word)
