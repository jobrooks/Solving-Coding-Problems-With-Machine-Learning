# 3.7 wrong answer 1/12
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_closest_palindrome(n):
    if is_palindrome(n):
        return n
    
    i = n + 1
    while not is_palindrome(i):
        i += 1
    
    j = n - 1
    while not is_palindrome(j):
        j -= 1
    
    if n - j <= i - n:
        return j
    else:
        return i

N = int(input())
for i in range(N):
    n = int(input())
    print(find_closest_palindrome(n))
