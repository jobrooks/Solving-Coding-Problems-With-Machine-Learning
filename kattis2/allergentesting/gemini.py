import math

def solve(n, d):
  """Returns the minimum number of sites needed to determine which of n compounds is the allergen within d days."""

  # If d is 1, then we can use 2 sites to test all n compounds.
  if d == 1:
    return 2

  # We can use binary search to find the minimum number of sites needed.
  low = 2
  high = n + 1

  while low < high:
    mid = (low + high) // 2

    # If we can determine the allergen within d days using mid sites, then we can also do it using mid - 1 sites.
    if can_determine(n, d, mid):
      high = mid
    # Otherwise, we need to use mid + 1 sites.
    else:
      low = mid + 1

  return low

def can_determine(n, d, m):
  """Returns True if we can determine which of n compounds is the allergen within d days using m sites."""

  # If we have more sites than compounds, then we can always determine the allergen within d days.
  if m > n:
    return True

  # Let's try to construct a schedule of tests that will allow us to determine the allergen within d days.
  schedule = [[] for _ in range(d)]

  # For each day, we will apply each compound to a unique subset of sites.
  for day in range(d):
    for i in range(n):
      schedule[day].append(set([i]))

  # Now, let's see if we can determine the allergen using this schedule.
  for day in range(d):
    # For each compound, let's see which sites it has been applied to so far.
    compound_sites = [set() for _ in range(n)]
    for i in range(n):
      for day2 in range(day + 1):
        compound_sites[i].update(schedule[day2][i])

    # If there is a site that has been applied to by only one compound, then that compound is the allergen.
    for site in range(m):
      applied_compounds = set()
      for i in range(n):
        if site in compound_sites[i]:
          applied_compounds.add(i)
      if len(applied_compounds) == 1:
        return True

  # If we cannot determine the allergen using this schedule, then we return False.
  return False

if __name__ == "__main__":
  t = int(input())

  for _ in range(t):
    n, d = map(int, input().split())
    print(solve(n, d))