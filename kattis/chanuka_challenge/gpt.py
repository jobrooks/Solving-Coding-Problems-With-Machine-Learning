# 1.3 accepted 2/2

# Function to calculate the number of candles needed for a given number of days
def calculate_candles(days):
    total_candles = 0
    for i in range(1, days+1):
        total_candles += i+1
    return total_candles

# Read the number of test cases
t = int(input())

# Loop through each test case
for i in range(1, t+1):
    # Read the data set number and number of days
    k, n = map(int, input().split())
    
    # Calculate the number of candles needed
    candles = calculate_candles(n)
    
    # Print the result
    print(k, candles)
