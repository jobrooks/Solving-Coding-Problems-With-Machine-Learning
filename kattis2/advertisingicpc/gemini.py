mod = int(998244353)

def main():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    # dp[i][j][mask]: the number of ways to fill the subgrid from (i, j) to the bottom-right, such that the subgrid is advertising ICPC and the top-left square has the specified mask

    dp = [[[[0 for _ in range(1 << 4)] for _ in range(m)] for _ in range(n)] for _ in range(4)]

    # Initialize the dp table for the bottom-right square

    for mask in range(1 << 4):
        if (mask & 3) == 3 and (mask >> 2 & 3) == 0:
            dp[n - 1][m - 1][mask] = 1

    # Fill the dp table from the bottom-right to the top-left

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            for mask in range(1 << 4):
                # Try filling the current square with a C, I, or P

                for letter in ["C", "I", "P"]:
                    new_mask = mask << 1
                    if letter == "C":
                        new_mask |= 1
                    elif letter == "I":
                        new_mask |= 1 << 2
                    else:
                        new_mask |= 1 << 3

                    # If the new mask is valid, add the number of ways to fill the rest of the subgrid to the current square

                    if (new_mask & 3) == 3 and (new_mask >> 2 & 3) == 0:
                        dp[i][j][mask] = (dp[i][j][mask] + dp[i][j + 1][new_mask] + dp[i + 1][j][new_mask] + dp[i + 1][j + 1][new_mask]) % mod

    # Output the number of ways to fill the entire grid

    print(dp[0][0][0])

if __name__ == "__main__":
    main()