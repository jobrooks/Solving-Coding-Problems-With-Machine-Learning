from collections import defaultdict

def get_lexicographically_smallest_string(n: int, m: int, conditions: list[tuple[int, int, int, int]]) -> str:
    """
    Finds the lexicographically smallest string s of textbf{even} length n consisting of 0 and 1,
    where s must satisfy m conditions.
    The i^{th} condition is represented by integers T_ i, L_ i, R_ i (1 leq L_ i<R_ i leq n), V_ i (0 leq V_ i).
    Note that L_ i notequiv R_ i text {(mod 2)}, or equivalently there is an textbf{even} number of elements within each range.
    If T_ i = 0, This means that there are at most V_ i more 0s than 1s in the L_ i^{th} and R_ i^{th} characters (inclusive) of s.
    If T_ i = 1, This means that there are at most V_ i more 1s than 0s in the L_ i^{th} and R_ i^{th} characters (inclusive) of s.
    Find the lexicographically smallest string s that satisfies all conditions.
    It can be proved that the constraints of the problem guarantee the existence of s that satisfies the conditions.

    Args:
    n: The length of the string.
    m: The number of conditions.
    conditions: A list of tuples representing the conditions.

    Returns:
    The lexicographically smallest string s that satisfies all conditions.
    """

    # Create a defaultdict to store the conditions for each character.
    conditions_for_characters = defaultdict(list)
    for condition in conditions:
        conditions_for_characters[condition[1]].append(condition)
        conditions_for_characters[condition[2]].append(condition)

    # Create a string of length n and set all characters to 0.
    s = '0' * n

    # Iterate over the characters in the string.
    for i in range(n):
        # Get the conditions for the current character.
        conditions_for_character = conditions_for_characters[i + 1]

        # If there are no conditions for the current character, skip to the next character.
        if not conditions_for_character:
            continue

        # If the current character is even, then the number of 0s and 1s in the range [L_i, R_i] must be equal.
        if i % 2 == 0:
            for condition in conditions_for_character:
                if condition[0] == 0:
                    s = s[:condition[1] - 1] + '0' * (condition[3] + 1) + s[condition[2]:]
                else:
                    s = s[:condition[1] - 1] + '1' * (condition[3] + 1) + s[condition[2]:]

        # If the current character is odd, then the number of 0s and 1s in the range [L_i, R_i] must differ by at most V_i.
        else:
            for condition in conditions_for_character:
                if condition[0] == 0:
                    if s[condition[1] - 1] == '0':
                        s = s[:condition[1] - 1] + '1' * (condition[3]) + s[condition[2]:]
                    else:
                        s = s[:condition[1] - 1] + '0' * (condition[3]) + s[condition[2]:]
                else:
                    if s[condition[1] - 1] == '1':
                        s = s[:condition[1] - 1] + '0' * (condition[3]) + s[condition[2]:]
                    else:
                        s = s[:condition[1] - 1] + '1' * (condition[3]) + s[condition[2]:]

    # Return the lexicographically smallest string.
    return s

# Sample Input 1
n1 = 6
m1 = 2
conditions1 = [(0, 1, 6, 2), (1, 5, 6, 1)]

# Sample Input 2
n2 = 6
m2 = 3
conditions2 = [(0, 1, 6, 0), (0, 1, 4, 0), (0, 3, 4, 0)]

# Print the lexicographically smallest string for each sample input
print(get_lexicographically_smallest_string(n1, m1, conditions1))  # Output 1: 000101 
print(get_lexicographically_smallest_string(n2, m2, conditions2))  # Output 2: 010101