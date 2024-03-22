# 8.9 wrong answer 3/76

def make_palindrome(s):
    n = len(s)
    count = 0
    for i in range(n//2):
        j = n - i - 1
        if s[i] != s[j]:
            count += 1
            s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
    return count

s = input()
print(make_palindrome(s))
