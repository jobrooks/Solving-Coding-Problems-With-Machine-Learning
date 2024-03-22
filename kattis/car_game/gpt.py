# 5.8 wrong answer 0/4
n, m = map(int, input().split())

# Create a dictionary of words where the key is the sorted
# set of characters in the word, and the value is the word itself
words = {}
for i in range(n):
    word = input().strip()
    sorted_word = ''.join(sorted(word))
    if sorted_word not in words:
        words[sorted_word] = word

# Process each license plate
for i in range(m):
    plate = input().strip()
    sorted_plate = ''.join(sorted(plate))

    # Find the first word in the dictionary that contains the characters
    # in the same order as the license plate
    found_word = False
    for key in words:
        if sorted_plate in key:
            print(words[key])
            found_word = True
            break

    if not found_word:
        print("No valid word")
