# 2.7 Error 1/11
from typing import List, Tuple

def solve(n: int, p: int, times: List[int]) -> Tuple[int, int]:
    """
    Args:
        n: The number of problems.
        p: The index of the problem to solve first.
        times: The time to solve each problem.

    Returns:
        The number of problems that can be solved and the penalty time.
    """

    # Check if the problem can be solved in time.
    if times[p] > 300:
        return 0, 0

    # Sort the problems in ascending order of time.
    times.sort()

    # Find the number of problems that can be solved.
    num_problems = 0
    for i in range(n):
        if i == p:
            continue
        if times[num_problems] + times[i] <= 300:
            num_problems += 1
        else:
            break

    # Find the penalty time.
    penalty_time = 0
    for i in range(num_problems):
        penalty_time += times[i]

    return num_problems, penalty_time


if __name__ == "__main__":
    # Read the input.
    n, p = map(int, input().split())
    times = list(map(int, input().split()))

    # Solve the problem.
    num_problems, penalty_time = solve(n, p, times)

    # Print the output.
    print(num_problems, penalty_time)