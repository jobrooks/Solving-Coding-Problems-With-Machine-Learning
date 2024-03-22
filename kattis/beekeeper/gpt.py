# 2.7 wrong answer 1/2

while True:
    n = int(input())
    if n == 0:
        break

    # initialize variables for the word with the most double vowels
    max_word = ''
    max_count = 0

    for i in range(n):
        word = input().strip()
        count = 0
        for j in range(len(word) - 1):
            if word[j] in 'aeiouy' and word[j] == word[j+1]:
                count += 1
        if count > max_count:
            max_word = word
            max_count = count

    print(max_word)
