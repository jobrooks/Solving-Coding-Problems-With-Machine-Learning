# 5.2 Error 1/9
def count_subsequences(string):
    a_count = 0
    b_count = 0
    c_count = 0
    for char in string:
        if char == 'A':
            a_count += 1
        elif char == 'B':
            b_count += 1
        elif char == 'C':
            c_count += 1

    a_count = a_count // 3
    b_count = b_count // 3
    c_count = c_count // 3

    return max(a_count, b_count, c_count)

string = input()
print(count_subsequences(string))