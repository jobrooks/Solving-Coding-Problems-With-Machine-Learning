# 3.2 accepted 94/94

s = input()

# Initialize the DP table with 26 lists (one for each letter)
dp = [[] for _ in range(26)]

# Iterate over each character in the string s
for i in range(len(s)):
    c = ord(s[i]) - ord('a')
    
    # Find the longest increasing subsequence ending at this character
    longest = []
    for j in range(c):
        if len(dp[j]) > len(longest) and dp[j][-1] < i:
            longest = dp[j]
    
    # Update the DP table for this character
    dp[c] = longest + [i]
    
# Find the length of the longest increasing subsequence over all letters
length = max(len(dp[i]) for i in range(26))

# The number of letters to add is the difference between the length of the
# longest increasing subsequence and the length of the alphabet (26)
print(26 - length)
