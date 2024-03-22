# Difficulty: 5.2
# Justification: 
# Result: Run-time error
# Tests passed: 0/33
# Error: run-time error
# Response: 
def arrange_tiles(prices_back, heights_back, prices_front, heights_front):
  """
  Finds a valid arrangement of tiles for the back and front rows, or determines if none exists.

  Args:
      prices_back: A list of prices for tiles in the back row (integers).
      heights_back: A list of heights for tiles in the back row (integers).
      prices_front: A list of prices for tiles in the front row (integers).
      heights_front: A list of heights for tiles in the front row (integers).

  Returns:
      A tuple containing two lists (back_row, front_row) representing a valid arrangement;
      "impossible" if no valid arrangement exists.
  """

  # Sort prices (and corresponding heights) in the front row (non-decreasing order)
  sorted_prices_front, sorted_heights_front = zip(*sorted(zip(prices_front, heights_front)))

  # Check if any tile in the front row is taller than a tile in the back row with the same price
  for price, height_front in zip(sorted_prices_front, sorted_heights_front):
    for i, (price_back, height_back) in enumerate(zip(prices_back, heights_back)):
      if price == price_back and height_front > height_back:
        return "impossible"  # Visibility constraint violated

  # Construct the back row arrangement by sorting the back row prices (and corresponding heights)
  # in reverse order (decreasing order to prioritize taller tiles in the back)
  back_row = [i + 1 for _, i in sorted(enumerate(zip(prices_back, heights_back)), key=lambda x: x[0], reverse=True)]

  # Construct the front row arrangement using the sorted prices from the front row (and corresponding heights)
  front_row = [sorted_prices_front.index(price) + 1 for price in prices_front]

  return back_row, front_row

# Read input
n = int(input())
prices_back = list(map(int, input().split()))
heights_back = list(map(int, input().split()))
prices_front = list(map(int, input().split()))
heights_front = list(map(int, input().split()))

# Find tile arrangement or determine impossibility
back_row, front_row = arrange_tiles(prices_back, heights_back, prices_front, heights_front)

# Print output
if back_row == "impossible":
  print(back_row)
else:
  print(*back_row)
  print(*front_row)
