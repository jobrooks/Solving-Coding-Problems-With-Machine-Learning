import sys

def main():
    # Read input
    ell, a, b, t, r = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    coffee_carts = list(map(int, sys.stdin.readline().split()))

    # Calculate the optimal time to get to the departure gate without buying coffee
    no_coffee_time = ell / a

    # Initialize the dp table
    dp = [[10**9 for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    # Iterate over the coffee carts
    for i in range(n):
        # Calculate the time to get to the current coffee cart
        time_to_cart = coffee_carts[i] / a

        # Iterate over the number of coffees already purchased
        for j in range(i + 1):
            # Calculate the time to get to the departure gate if we buy coffee at the current cart
            time_with_coffee = time_to_cart + t + r + (ell - coffee_carts[i]) / b

            # Update the dp table
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + time_with_coffee)

    # Find the minimum time to get to the departure gate
    min_time = 10**9
    for j in range(n + 1):
        min_time = min(min_time, dp[n][j])

    # Check if it is possible to get to the departure gate on time
    if min_time > no_coffee_time:
        print(-1)
        return

    # Reconstruct the optimal solution
    i = n
    j = 0
    coffee_carts_used = []
    while i > 0:
        if dp[i][j] < dp[i - 1][j]:
            coffee_carts_used.append(i - 1)
            j += 1
        i -= 1

    # Print the output
    print(len(coffee_carts_used))
    print(' '.join(map(str, coffee_carts_used)))

if __name__ == '__main__':
    main()